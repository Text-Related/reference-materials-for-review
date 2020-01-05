import sqlite3

con = sqlite3.connect(r"D:\code\adroiddatabase\ad.db")

cur = con.execute("select * from ad")

for row in cur:
    print(row)

cur.close()
