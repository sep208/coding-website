from db import get_db

def create_users_table():
    connection = get_db()
    cursor = connection.cursor()
    
    create_table_query = """
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT,
            email TEXT,
            password TEXT
        );
    """

    cursor.execute(create_table_query)
