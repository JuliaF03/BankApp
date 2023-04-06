#connect to pgAdmin
import psycopg2

for i in range(3):
    try:
        connection = psycopg2.connect(
            host = "localhost",
            database = "teste",
            user = "postgres",
            password = "bembom",
            port = "5432"
        )

    except:
        print('Cannot access database.\n')
        continue

    else:
        print("Database connected.\n")
        break

