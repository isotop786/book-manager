import sqlite3

conn = sqlite3.connect("lite.db")
cursor = conn.cursor()

#cursor.execute("CREATE TABLE store (id INTEGER PRIMARY KEY, item TEXT,quantity INTEGER, price REAL)")

#cursor.execute("insert into store(item, quantity, price) values('book',5,20)")

res = cursor.execute("select * from store")
for x in res:
    print(x[1])

#conn.commit()