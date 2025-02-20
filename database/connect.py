import psycopg2
def connection_db():
    conn = psycopg2.connect(
        database="the_bear",
        password="admin",
        user="admin",
        host="localhost",
        port="5432"
        )
    return conn

# Call the function to test the connection
connection = connection_db()
print(connection)
connection.close()
print(connection)


