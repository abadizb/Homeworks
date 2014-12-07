import sqlite3
conn = sqlite3.connect("zoo.sqlite")
cursor = conn.cursor()

cursor.execute("Create table animal_count (name , count)")

animal = input("Enter an animal:")
count = input ("Enter a count")
cursor.execute("insert into animal_count(name, count)values(?,?)",(animal,count))

result = cursor.execute("select * from animal_count")

for row in result:
    print (row)

conn.commit()
conn.close()
