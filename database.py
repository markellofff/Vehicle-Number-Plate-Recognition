import sqlite3

# creating the table
def create_table():
    # establishing connection
    db = sqlite3.connect("RTO.db")
    # invoking cursor
    my_cur = db.cursor()
    # sql for creating the table
    sql = '''CREATE TABLE details 
            (`Name` text, `vehicle_no` text,`address` text )'''
    my_cur.execute(sql)
    print("created")

# use the below function only once
# create_table()


# for populating your table
def insert_into_table(Name, Vehicle_no, address):
    db = sqlite3.connect("RTO.db")
    my_cur = db.cursor()
    sql = '''INSERT INTO details (Name , vehicle_no, address)
            VALUES (?,?,?);'''
    values = [Name, Vehicle_no, address]
    my_cur.execute(sql, values)
    db.commit()
    print("inserted")

# Don't run the same vehicle no more than one time otherwise 2 records will be displayed at every time.

# insert_into_table("Robin", "AB 20 XY 1234", "Berlin")

# Manual searching for a data
def search(vehicle_no):
    db = sqlite3.connect("RTO.db")
    my_cur = db.cursor()
    my_cur.execute("""SELECT * FROM details WHERE vehicle_no='{}'""".format(vehicle_no))
    for z in my_cur.fetchall():
        print("Name :", z[0])
        print("Vehicle No. :", z[1])
        print("Address :", z[2])


# search("ABX 2030")


def delete_rec(vehicle_no):
    db = sqlite3.connect("RTO.db")
    my_cur = db.cursor()
    my_cur.execute("""DELETE FROM details WHERE vehicle_no = '{}'""".format(vehicle_no))
    db.commit()
    print("Deleted")


# delete_rec("AB 20 XY 1234")



"""Uuncomment the following chunk and run only once then your table is populated with the records"""
# db = sqlite3.connect('RTO.db')
# my_cur = db.cursor()
# vals = [("Andy murray", "ABX 2030", "New York"), ("Tony Stark", "STARK 1", "Bleaker's street, New York")]
# sql = """INSERT INTO details (Name, vehicle_no, address)
#             VALUES(?, ?, ?)"""
#
# my_cur.executemany(sql, vals)
# db.commit()
# db.close()
# print("done")