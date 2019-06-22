import names
import pandas as pd
import pymongo
import pymssql
import random
import string
import timeit


MOVIE_LIMIT = 500_001

CATEGORY = 100
ACTOR = 100




def random_name(length):
    return ''.join(random.choice(string.ascii_letters+string.digits) for _ in range(length))

# cursor - mssql cursor
# conn - mssql connection
# mongo_db - mongo db
def fight(n_movies, cursor, conn, mongo_db):
    conn.commit()

    def run_mssql_test():
        cursor.execute(
        "SELECT \n"
        "d.id as 'ID',  \n"
        "d.firstName as 'Imię',\n"
        "d.lastName as 'Nazwisko',\n"
        "d.birthDate  'Data urodzenia', \n"
        "sum(m.budget) as 'Suma budżetów filmów',\n"
        "avg(m.rating) as 'Średnia ocena filmów',\n"
        "(\n"
        "    SELECT COUNT(r.idMovie)\n"
        "    FROM Movie m, Role r\n"
        "    WHERE m.id = r.idMovie\n"
        "    AND m.Director = d.id\n"
        ") as 'Łączna liczba bohaterów w filmach'\n"
        "FROM Director d INNER JOIN Movie m\n"
        "ON (m.Director = d.id)\n"
        "GROUP BY d.id, d.firstName, d.lastName, d.birthDate\n"
        "HAVING sum(m.budget) > 100000\n"
        )
        x = cursor.fetchall()
        #print(f'Zanaleziono {len(x)} wynikow, pierwszy wynik to:')
        #print(x[0])

    mssqlTime = timeit.Timer(lambda: run_mssql_test()).timeit(number=1)
    
    def run_mongo_test():
        x = db.Director.aggregate([
            {"$group" : {"_id" : "$lastName", 
                "count":{"$sum":"$movies.budget"}, 
                "count":{"$avg":"$movies.rating"},
                "count":{"$movies.roles"}
            }}
        ])
        #print(f'Zanaleziono {len(x)} wynikow, pierwszy wynik to:')
        #print(x[0])
    mongoTime = timeit.Timer(lambda: run_mssql_test()).timeit(number=1)

    print(f'{n_movies} filmów -> MS SQL Server: {mssqlTime} vs MongDB: {mongoTime}')


if __name__ == "__main__":
    # Obiekty obslugi mssql (oraz czyszczenie zawartosci bazy danych)
    conn = pymssql.connect(host='127.0.0.1:1433', user='SA', password='Pp1234567!')
    cursor = conn.cursor()
    cursor.execute('USE SBD_LAB_4')
    cursor.execute('DELETE FROM Role')
    cursor.execute('DELETE FROM Movie')
    cursor.execute('DELETE FROM Category')
    cursor.execute('DELETE FROM Actor')
    cursor.execute('DELETE FROM Director')
    

    # Obiekty obslugi mongodb (oraz czyszczenie zawartosci bazy danych)
    client = pymongo.MongoClient()
    client.drop_database('sbdlab4_mongo')
    db = client.sbdlab4_mongo

    # Lista aktorow i kategorii wykorzystywane w pozniejszym generowaniu danych
    actors = []
    category = []

    for i in range(CATEGORY):
        name = random_name(20)
        description = random_name(45)
        obj = {
            'name':name,
            'description': description
        }
        obj['mongo_id'] = db.Category.insert_one(obj).inserted_id
        obj['id'] = i
        category.append(obj)
        cursor.execute(f"INSERT INTO Category (id, name, description) VALUES ({i},'{name}','{description}')")


    for i in range(ACTOR):
        firstName = names.get_first_name() 
        lastName = names.get_last_name()
        birthDate = f'{str(random.randint(1980,1995)).zfill(4)}-{str(random.randint(1,12)).zfill(2)}-{str(random.randint(1,28)).zfill(2)}'
        obj = {
            'id':i,
            'firstName': firstName,
            'lastName': lastName,
            'birthDate': birthDate
        }   
        obj['mongo_id'] = db.Actor.insert_one(obj).inserted_id
        obj['id'] = i
        actors.append(obj)
        cursor.execute(f"INSERT INTO Actor (id, firstName, lastName, birthDate) VALUES ({i}, '{firstName}','{lastName}','{birthDate}')")

    actors = pd.DataFrame(actors)
    category = pd.DataFrame(category)
    
    # Generowanie danych
    movies_generated = 0
    directors_generated = 0
    roles_generated = 0

    director_insert = []
    movie_insert = []
    role_insert = []

    while movies_generated <= MOVIE_LIMIT: # Create directors

        
        director_firstName = names.get_first_name()
        director_lastName = names.get_last_name()
        director_birthDate = f'{str(random.randint(1980,1995)).zfill(4)}-{str(random.randint(1,12)).zfill(2)}-{str(random.randint(1,28)).zfill(2)}'

        director =  {'firstName': director_firstName, 'lastName':director_lastName, 'birthDate': director_birthDate, 'movies':[]} 
        director_insert.append(
            (directors_generated, director_firstName, director_lastName, director_birthDate)
        )
        

        for _ in range(random.randint(5,20)): # Create movies
            movie_name = random_name(20)
            movie_Director = directors_generated
            movie_releaseDate = f'{str(random.randint(2000,2005)).zfill(4)}-{str(random.randint(1,12)).zfill(2)}-{str(random.randint(1,28)).zfill(2)}'
            movie_Cathegory = random.randint(0, CATEGORY-1)
            movie_length = random.randint(60, 200)
            movie_budget = random.randint(1_000_000, 20_000_000)
            movie_rating = random.randint(0,10)

            movie = {
                'name': movie_name,
                'releaseDate': movie_releaseDate,
                'Category': category.iloc[movie_Cathegory]['mongo_id'],
                'length': movie_length,
                'budget': movie_budget,
                'rating': movie_rating,
                'roles':[]
            }
            director['movies'].append(movie)
            movie_insert.append(
                (movies_generated, movie_name, movie_Director, movie_releaseDate, movie_Cathegory, movie_length, movie_budget, movie_rating)
            )
            for _ in range(random.randint(3,10)): # Crate roles
                role_idMovie = movies_generated
                role_idActor = random.randint(0, ACTOR-1)
                role_characterName = names.get_full_name()

                role = {'idActor': actors.iloc[role_idActor]['mongo_id'], 'characterName': role_characterName}
                movie['roles'].append(role)
                role_insert.append(
                    (role_idMovie, role_idActor, role_characterName)
                )
                roles_generated +=1
            movies_generated += 1
            if movies_generated != 0 and movies_generated % 1000 == 0:
                    cursor.executemany('INSERT INTO Director (id, firstName, lastName, birthDate) VALUES (%s, %s, %s, %s)', director_insert)
                    cursor.executemany('INSERT INTO Movie (id, name, Director, releaseDate, Category, length, budget, rating) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)', movie_insert)
                    cursor.executemany('INSERT INTO Role (idMovie, idActor, characterName) VALUES (%s, %s, %s)', role_insert)
                    director_insert = []
                    movie_insert = []
                    role_insert = []
                    fight(movies_generated, cursor, conn, db)

            if movies_generated >= MOVIE_LIMIT: # Break if all movies generated
                break
        
        db.Director.insert_one(director)
        directors_generated += 1
    conn.commit()
    conn.close()