from db import cursor, conn
#insert
def ins():
    name=input("enter your name:")
    salary=float(input("enter your salary:"))
    cursor.execute("insert into emp(name,salary) values(%s,%s)",(name,salary))
    conn.commit()   
    print("data inserted")