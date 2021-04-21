from db import get_db
from werkzeug.security import generate_password_hash

def signup_user(username, email, password):
    connection = get_db()
    cursor = connection.cursor()
    
    signup_query = """
        INSERT INTO users (username, email, password)
        VALUES (?, ?, ?);
    """
    
    hashed_password = generate_password_hash(password)
    
    cursor.execute(signup_query, [username, email, hashed_password])
    connection.commit()
