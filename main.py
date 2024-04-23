import sqlite3

# connect to a database

conn = sqlite3.connect("./tutorial.db")

#initializing a cursor

db_cursor = conn.cursor()

# db_cursor.execute("CREATE TABLE movies(title, year, score)")

def table_exists(cursor, table_name):
	stmt = "SELECT name FROM sqlite_master WHERE name='%s'"
	print(stmt % table_name)
	result = cursor.execute(stmt % table_name)
	if result.fetchone() != None:
		return True
	else:
		return False

def bulk_insert_movies(cursor, table_name, data, c):
	stmt = "INSERT INTO %s VALUES(?, ?, ?)"
	if table_exists(cursor, table_name):
		cursor.executemany(stmt % table_name, data)
	c.commit()
		
m = [("Batman", 1999, 10), ("Spider Man", 2009, 6.3)]
bulk_insert_movies(db_cursor, "movies", m, conn)

query_res = db_cursor.execute("SELECT title from movies")
print(query_res.fetchall())

print("Success!")
# conn.commit()


