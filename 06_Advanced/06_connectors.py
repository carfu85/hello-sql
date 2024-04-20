# CONNECTORS
# Lección 19.1: https://youtu.be/OuJerKzV5T0?t=20876
# Lección 19.2: https://youtu.be/OuJerKzV5T0?t=21149

# Ejemplo de conexión desde Python a una base de datos local
# Se ejemplifica cómo evitar SQL INJECTION
import mysql.connector


def print_user(user):

    config = {
        "host": "127.0.0.1",
        "port": "3306",
        "database": "hello_mysql",
        "user": "root",
        "password": "root1234"
    }

    # config = {
    #     "host": "bpw0hq9h09e7mqicjhtl-mysql.services.clever-cloud.com",
    #     "port": "3306",
    #     "database": "bpw0hq9h09e7mqicjhtl",
    #     "user": "uqzby88erlhvkrty",
    #     "password": "oePXiCOHdU1WRV80NPyv"
    # }

    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()

    query = "SELECT * FROM users WHERE name=%s;"
    print(query)
    cursor.execute(query, (user,))
    result = cursor.fetchall()

    for row in result:
        print(row)

    cursor.close()
    connection.close()


print_user("Brais")
# print_user("'; UPDATE users SET age = '15' WHERE user_id = 1; --")


POSTGRESQL_ADDON_HOST=bhbju4gwhychlwvc2wib-postgresql.services.clever-cloud.com
POSTGRESQL_ADDON_DB=bhbju4gwhychlwvc2wib
POSTGRESQL_ADDON_USER=ura07ny6utvs8freweuy
POSTGRESQL_ADDON_PORT=50013
POSTGRESQL_ADDON_PASSWORD=nCsAGy9JomO2sz72IiVD7p4hxv24uY
POSTGRESQL_ADDON_URI=postgresql://ura07ny6utvs8freweuy:nCsAGy9JomO2sz72IiVD7p4hxv24uY@bhbju4gwhychlwvc2wib-postgresql.services.clever-cloud.com:5432/bhbju4gwhychlwvc2wib