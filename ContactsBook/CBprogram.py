import sqlite3

conn = sqlite3.connect
('ContactBookProrgram.db')

cur = conn.cursor()
cur.execute('SELECT * from Name')
"""
print(cur.fetchone())
"""