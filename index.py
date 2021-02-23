import sqlite3
conn = sqlite3.connect('main.sqlite')
c = conn.cursor()
rows = c.execute("SELECT * FROM active;").fetchall()
print(rows)
