import sqlite3

#set up database
conn = sqlite3.connect("yourdb.db")
cursor = conn.cursor()
cursor.execute("""CREATE TABLE filmdb(year TEXT, title TEXT, genre TEXT)""")
conn.commit()

#insert base data
films = [
    ("2011", "Brothers", "Drama"),
    ("2002", "Spider Man", "Sci Fi"),
    ("2009", "WatchMen", "Drama"),
    ("2010", "Inception", "Sci Fi"),
    ("2009", "Avatar", "Fantasy"),
    ]
cursor.executemany("INSERT INTO filmdb VALUES (?,?,?)", films)
conn.commit()

#Show all the movies in the database
showall = """SELECT * FROM filmdb"""
cursor.execute(showall)
print("All the films currently in the database")
output = cursor.fetchall()
for row in output:
    print(row)

#Show the movie brothers
print("\n\nThe details of the film, Brothers, are: ")
showfilm = """SELECT * FROM filmdb WHERE title ="Brothers";"""
row = cursor.fetchall()
for row in cursor.execute(showfilm):
    print(row)

#Show the films from 2009
print("\n\nThe details of the films from 2009 are: ")
showfilm = """SELECT * FROM filmdb WHERE year ="2009";"""
row = cursor.fetchall()
for row in cursor.execute(showfilm):
    print(row)

#Show the drama and fantasy films
print("\n\nThe drama and fantasy films are: ")
showfilm = """SELECT * FROM filmdb WHERE genre = "Fantasy" OR genre = "Drama";"""
row = cursor.fetchall()
for row in cursor.execute(showfilm):
    print(row)
    
#Delete all data then show empy DB
cursor.execute("DELETE FROM filmdb")
showall = """SELECT * FROM filmdb"""
cursor.execute(showall)
print("\n\nAll the films currently in the database")
output = cursor.fetchall()
for row in output:
    print(row)


conn.close()