import sqlite3

conn = sqlite3.connect("historial_loggs.db")
cursor = conn.cursor()

cursor.executescript("""
CREATE INDEX IF NOT EXISTS idx_hora_envio ON historial_loggs(hora_envio);
CREATE INDEX IF NOT EXISTS idx_hora_recibida ON historial_loggs(hora_recibida);
CREATE INDEX IF NOT EXISTS idx_service ON historial_loggs(service);
CREATE INDEX IF NOT EXISTS idx_severity ON historial_loggs(severity);
""")
conn.commit()
conn.close()