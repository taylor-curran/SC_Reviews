import sqlite3

# Right Click on DB and Click [Copy Relative Path]
db_path_packed = '../Study_Guides_Distribute_Repo/data/Chinook_Sqlite.sqlite'

conn_packed = sqlite3.connect(db_path_packed)
curs_packed = conn_packed.cursor()

# Test Connection
response = curs_packed.execute("SELECT * FROM Track;").fetchall()

