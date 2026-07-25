from db import conn,cursor

# insert
def insert_emp():
    name=input("enter yr name \n")
    sal=int(input("enter yr sal\n"))
    query="insert into emp (name,sal) values(%s,%s)"
    values=(name,sal)
    cursor.execute(query,values)
    conn.commit()
    print("data inserted!")