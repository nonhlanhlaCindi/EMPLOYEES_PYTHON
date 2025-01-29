import psycopg2

def get_db_connection():
    conn = psycopg2.connect(
        dbname="mycompany",
        user="postgres",  # Replace with your PostgreSQL username
        password="my_password",  # Replace with your PostgreSQL password
        host="localhost",
        port="5432"
    )
    return conn