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
# c.execute("DELETE FROM nv")
# c.execute("INSERT INTO nv VALUES('NVIDIA GeForce GT 710 CBR 2Gb',5000)")
# c.execute("INSERT INTO nv VALUES( 'NVIDIA GeForce RTX 2060 super', 25000)")
#
# c.execute("INSERT INTO nv VALUES('NVIDIA GeForce GTX 1650 4 Гб',20000)")
# c.execute("INSERT INTO nv VALUES('NVIDIA GeForce RTX 3060 8 Гб',39000)")
# c.execute("INSERT INTO nv VALUES('NVIDIA GeForce RTX 4060 Ti 8 Гб',53000)")
# c.execute("INSERT INTO nv VALUES('NVIDIA GeForce RTX 4060 Ti Palit JetStream 16Gb',58000)")
# c.execute("INSERT INTO nv VALUES('NVIDIA GeForce RTX 4070 Gigabyte 12Gb',70000)")


# c.execute("INSERT INTO rd VALUES('AMD Radeon RX 550 PowerColor Red Dragon 2Gb ',7000)")
# c.execute("INSERT INTO rd VALUES('AMD Radeon RX 6500 XT PowerColor 4Gb ',20000)")
# c.execute("INSERT INTO rd VALUES('AMD Radeon RX 6600 Sapphire 8Gb ',26000)")
# c.execute("INSERT INTO rd VALUES('AMD Radeon RX 7600 XT ASRock Steel Legend OC 16Gb ',48000)")
# c.execute("INSERT INTO rd VALUES('AMD Radeon RX 7800 XT ASUS 16Gb ',64000)")
# c.execute("INSERT INTO rd VALUES('AMD Radeon RX 7900 XT Sapphire Gaming OC 20Gb',104000)")




# c.execute("INSERT INTO rizen VALUES('AMD A6-9500 OEM','CBR A320M',9000)")
# c.execute("INSERT INTO intel VALUES('Intel Celeron G4900 OEM','ASUS PRIME H310M-K R2.0',9000)")
#
# c.execute("INSERT INTO rizen VALUES('AMD Ryzen 5 3600X OEM','MSI A520M-A PRO',16000)")
# c.execute("INSERT INTO intel VALUES(' Intel Core i3 - 12100F OEM','Gigabyte H610M K DDR4',15000)")
#
# #то же
# c.execute("INSERT INTO intel VALUES('Intel Core i5 - 12400F OEM','Gigabyte B760M DS3H DDR4',23000)")
#
# c.execute("INSERT INTO rizen VALUES('AMD Ryzen 5 5600X OEM','Gigabyte B550 GAMING X V2 (DDR4)',24000)")
# #то же
#
# c.execute("INSERT INTO rizen VALUES('AMD Ryzen 5 7500F OEM','MSI PRO B650M-A WIFI',40000)")
# c.execute("INSERT INTO intel VALUES(' Intel Core i5 - 13400F OEM','GMSI B760 GAMING PLUS WIFI',33000)")
#
# c.execute("INSERT INTO rizen VALUES('AAMD Ryzen 5 7600X3D OEM','ASRock A620M PRO RS',56000)")
# c.execute("INSERT INTO intel VALUES(' Intel Core i7 - 14700KF OEM','MSI PRO Z790-P WIFI',67000)")


# c.execute("INSERT INTO otherset VALUES('ID-COOLING DK-01S','8Gb DDR4 2666MHz KingSpec','450W ExeGate AA450',3500)")
# c.execute("INSERT INTO otherset VALUES('DeepCool AG300',' 2x 8Gb DDR4 3200MHz Crucial','500W DeepCool PF500',7000)")
# c.execute("INSERT INTO otherset VALUES(' ID-COOLING SE-224-XTS','16Gb DDR4 3200MHz Kingston Fury Beast Black (2x8Gb KIT)','650W DeepCool PF650',13000)")
# c.execute("INSERT INTO otherset VALUES('ID-COOLING SE-224-XTS','16Gb DDR4 3200MHz Kingston Fury Beast Black (2x8Gb KIT)','750W DeepCool PF750',14000)")
# c.execute("INSERT INTO otherset VALUES(' ID-COOLING SE-224-XTS','32Gb DDR5 6400MHz ADATA XPG Lancer Blade White(2x16Gb KIT)','750W DeepCool PF750',21000)")
c.execute("SELECT * FROM otherset ORDER BY priceSum DESC")
itoth = c.fetchall()
print(itoth)
c.execute("SELECT * FROM intel ORDER BY price DESC")
itint = c.fetchall()
c.execute("SELECT * FROM rizen ORDER BY price DESC")
itrizen = c.fetchall()


c.execute("SELECT * FROM nv ORDER BY price DESC")
itemsnv = c.fetchall()
c.execute("SELECT * FROM rd ORDER BY price DESC")
itemsrd = c.fetchall()
# for el in items:
#     if(el[1] <6000):
#         print(el[0])
# for el in items:
#     print(el[0] + str(el[1]))
db.commit()
db.close()
