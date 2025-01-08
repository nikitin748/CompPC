import sqlite3

db = sqlite3.connect('comp.db')
c = db.cursor()
# c.execute("""CREATE TABLE nv (
#     model text,
#     price integer
# )""")
# c.execute("""CREATE TABLE rd (
#     model text,
#     price integer
# )""")
# c.execute("""CREATE TABLE rizen (
#     model text,
#     motherboard text,
#     price integer
# )""")
# c.execute("""CREATE TABLE intel (
#     model text,
#     motherboard text,
#     price integer
# )""")
# c.execute("""CREATE TABLE otherset (
#     cooler text,
#     RAM text,
#     bp text,
#     priceSum integer
# )""")
# c.execute("INSERT INTO nv VALUES('NVIDIA GeForce GT 710 CBR 2Gb',5500)")
#c.execute("UPDATE nv SET model = 'NVIDIA GeForce RTX 2060 super' WHERE price = 25000")
c.execute("SELECT * FROM nv ORDER BY price DESC")
items = c.fetchall()
# for el in items:
#     if(el[1] <6000):
#         print(el[0])
for el in items:
    print(el[0] + str(el[1]))
db.commit()
db.close()
