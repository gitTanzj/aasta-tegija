import sqlite3 as sql

def databaseInit(tables):
    conn = sql.connect('Vocostarter.db')
    c = conn.cursor()

    for i in tables:
        c.execute(f'CREATE TABLE {i} ("SKOOR" INTEGER DEFAULT 0)')
        print(f'created table {i}')

    conn.commit()
    conn.close()
