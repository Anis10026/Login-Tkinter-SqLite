import sqlite3
def init_db():
    #connecion a la base de donnée
    conn=sqlite3.connect("utilisateurs.db")
    cursor=conn.cursor()

    #Creation de la table des utilisateurs
    cursor.execute("""
         CREATE TABLE IF NOT EXISTS users(
             id INTEGER PRIMARY KEY AUTOINCREMENT,
             username TEXT UNIQUE NOT NULL,
             password TEXT NOT NULL)
             """)

    cursor.execute("SELECT COUNT(*)FROM users")
    if cursor.fetchone()[0]==0:
        cursor.execute("INSERT INTO users(username,password)VALUES(?,?)",("anisanis","12364"))
        conn.commit()
    conn.close()


init_db()
