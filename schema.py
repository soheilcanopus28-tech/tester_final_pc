import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

db_url = os.getenv('DATABASE_URL')

def create_table():
    conn = psycopg2.connect(db_url)
    cursor = conn.cursor()

    #questions
    cursor.execute(
    '''
        CREATE TABLE IF NOT EXISTS questions(
            id SERIAL PRIMARY KEY ,
            question TEXT NOT NULL,
            option1 TEXT NOT NULL,
            option2 TEXT NOT NULL,
            option3 TEXT NOT NULL,
            option4 TEXT NOT NULL,
            correct_option INTEGER NOT NULL
    
    
    )
    '''
    )

    # Results
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS results (           
            id SERIAL PRIMARY KEY ,
            user_id INTEGER NOT NULL,
            score INTEGER NOT NULL,
            date DATETIME DEFAULT CURRENT_TIMESTAMP     
        )
    ''')
    
    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_table()
    print('tables created successfuly.')