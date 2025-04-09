import mariadb
db_config = {
    'host': '10.100.10.104',
    'port': 3306,
    'user': 'martin',
    'password': 'Hei',
    'database': 'eksamenting'
}

def get_db_connection():
    try:
        connection = mariadb.connect(**db_config)
        return connection
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB: {e}")
        return None
