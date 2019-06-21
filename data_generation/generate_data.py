import random
import string

MOVIE_1 = 100000
MOVIE_2 = 250000
MOVIE_3 = 500000

ROLE_1 = 100000
ROLE_2 = 250000
ROLE_3 = 500000


CATEGORY = 1000
DIRECTOR = 1000
ACTOR = 2000

def random_name(length):
    return ''.join(random.choice(string.ascii_letters+string.digits) for _ in range(length))


with open('movies1.csv', 'w') as f:
    f.write('id,name,Director,releaseDate,Category,length,budget,rating\n')
    for i in range(MOVIE_1):
        f.write(
                f'{i},' # id
                f'{random_name(20)},' # name
                f'{random.randint(0, DIRECTOR-1)},' # Director
                f'{random.randint(1,29)}-{random.randint(1,12)}-{random.randint(2000,2005)},' # releaseDate
                f'{random.randint(0,CATEGORY-1)},' # Category
                f'{random.randint(60,200)},' # length
                f'{random.randint(1000000,20000000)},' # budget
                f'{random.randint(0,10)}\n' # rating

        )



with open('movies2.csv', 'w') as f:
    f.write('id,name,Director,releaseDate,Category,length,budget,rating\n')
    for i in range(MOVIE_2):
        f.write(
                f'{i},' # id
                f'{random_name(20)},' # name
                f'{random.randint(0, DIRECTOR-1)},' # Director
                f'{random.randint(1,29)}-{random.randint(1,12)}-{random.randint(2000,2005)},' # releaseDate
                f'{random.randint(0,CATEGORY-1)},' # Category
                f'{random.randint(60,200)},' # length
                f'{random.randint(1000000,20000000)},' # budget
                f'{random.randint(0,10)}\n' # rating

        )



with open('movies3.csv', 'w') as f:
    f.write('id,name,Director,releaseDate,Category,length,budget,rating\n')
    for i in range(MOVIE_3):
        f.write(
                f'{i},' # id
                f'{random_name(20)},' # name
                f'{random.randint(0, DIRECTOR-1)},' # Director
                f'{random.randint(1,29)}-{random.randint(1,12)}-{random.randint(2000,2005)},' # releaseDate
                f'{random.randint(0,CATEGORY-1)},' # Category
                f'{random.randint(60,200)},' # length
                f'{random.randint(1000000,20000000)},' # budget
                f'{random.randint(0,10)}\n' # rating

        )

with open('role1.csv', 'w') as f:
    f.write('idMovie,idActor,characterName\n')
    for i in range(ROLE_1):
        f.write(
                f'{random.randint(0,MOVIE_1-1)},' # idMovie
                f'{random.randint(0,ACTOR-1)},' # idActor
                f'{random_name(20)}\n' # characterName

        )

with open('role2.csv', 'w') as f:
    f.write('idMovie,idActor,characterName\n')
    for i in range(ROLE_2):
        f.write(
                f'{random.randint(0,MOVIE_2-1)},' # idMovie
                f'{random.randint(0,ACTOR-1)},' # idActor
                f'{random_name(20)}\n' # characterName

        )
with open('role3.csv', 'w') as f:
    f.write('idMovie,idActor,characterName\n')
    for i in range(ROLE_3):
        f.write(
                f'{random.randint(0,MOVIE_3-1)},' # idMovie
                f'{random.randint(0,ACTOR-1)},' # idActor
                f'{random_name(20)}\n' # characterName

        )


with open('categories.csv', 'w') as f:
    f.write('id,name,description\n')
    for i in range(CATEGORY):
        f.write(
                f'{i},' # id
                f'{random_name(20)},' # name
                f'{random_name(45)}\n' # description

        )

with open('directors.csv', 'w') as f:
    f.write('id,firstName,lastName,birthDate\n')
    for i in range(DIRECTOR):
        f.write(
                f'{i},' # id
                f'{random_name(20)},' # firstName
                f'{random_name(20)},' # lastName
                f'{random.randint(1,29)}-{random.randint(1,12)}-{random.randint(2000,2005)}\n' # birthDate
        )

with open('actors.csv', 'w') as f:
    f.write('id,firstName,lastName,birthDate\n')
    for i in range(ACTOR):
        f.write(
                f'{i},' # id
                f'{random_name(20)},' # firstName
                f'{random_name(20)},' # lastName
                f'{random.randint(1,29)}-{random.randint(1,12)}-{random.randint(2000,2005)}\n' # birthDate
        )
