import sqlite3

conn = sqlite3.connect("historial_loggs.db")
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS historial_loggs (
               id_historial INTEGER PRIMARY KEY AUTOINCREMENT,
               hora_envio TEXT NOT NULL,
               service TEXT NOT NULL,
               severity TEXT NOT NULL, 
               message TEXT NOT NULL,
               hora_recibida TEXT NOT NULL
               )
""")
conn.commit()
conn.close()