# SBD_LAB4
Rozproszone bazy danych


# Konfiguracja bazy danych
Obie bazy danych zostały uruchomione na systemie Ubuntu 18.04 jako kontenery docker.

# Komendy

## Instalacja narzędzi i tworzenie bazy danych:
**Instalacja docker:**

  `sudo apt-get install docker.io`

  **Utworzenie bazy danych MongDB:**

  `sudo docker run -d -p=27017:27017 --name=sbdlab4_mongo mongo`

  lub

  `sudo docker run -d -p=27017:27017 -v ~/Desktop/SBD_LAB_4/mongodb_data:/data/db --name=sbdlab4_mongo mongo`
  jeśli się chce zapisywać dane w określonej ścieżce.

  **Utworzenie bazy danych MS SQL:**

  `sudo docker run -e 'ACCEPT_EULA=Y' -e 'SA_PASSWORD=Pp1234567!' -p 1433:1433 -d --name=sbdlab4_mssql mcr.microsoft.com/mssql/server:2017-latest`

  User (domyślny) "sa" hasło "Pp1234567!"

  **Klient do obsługi mongodb**:
  
  Instalacja:

  `sudo apt-get install mongodb-clients`

  Uruchomienie:

  `mongo localhost/sbdlab4_mongo`

  **Pobranie klienta do obsługi MS SQL:**

  Baza danych MS SQL jest obsługiwana za pomocą DBever. https://dbeaver.io/

## Usunięcie bazy danych:
  **Zatrzymanie kontenera sbdlab4_mongo:**

  `sudo docker stop sbdlab4_mongo`

  **Usunięcie kontenera sbdlab4_mongo:**

  `sudo docker rm sbdlab4_mongo`

  **Usunięcie nieużywanych przez docker volume:**

  `sudo docker volume prune`

  **Usunięcie nieużywanych przez docker elementów:**

  `sudo docker system prune`

## Inne

  **Lista wszystkich kontenerów w docker:**

  `sudo docker ps -a`

  **Lista wszystkich volume w docker:**

  `sudo docker volume ls`


