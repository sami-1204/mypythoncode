import  sqlite3
conn = sqlite3.connect("student.db")

cursor=conn.cursor()

cursor.execute('''
    create table if not exists stud(
                sid integer primary key,
                name text not null,
                age integer null)    
 ''')

print("created!")
cursor.execute("insert into stud (sid,name,age) values(?,?,?)",(sid,sname,age))
cursor.execute("insert into stud (sid,name,age) values(?,?,?)",(sid,sname,age))
cursor.execute("insert into stud (sid,name,age) values(?,?,?)",(sid,sname,age))
cursor.execute("insert into stud(sid,name,age) values(?,?,?)",(2,"diksha","21"))
cursor.execute("insert into stud(sid,name,age) values(?,?,?)",(3,"mansi","20"))
cursor.execute("insert into stud(sid,name,age) values(?,?,?)",(4,"yash","22"))

conn.commit()
print("data inserted")

sid= int(input("enter id :"))
sname=input("enter name :")
age=int(input("enter age : "))
cursor.execute("insert into stud (sid,name,age) values(?,?,?)",(sid,sname,age))
conn.commit()
print("data inserted")

  
cursor.execute("select * from stud")
rows=cursor.fetchall()
print(rows)

for r in rows:
    print(f"{r[0]}")

sid= int(input("enter id\n :"))
cursor.execute("select * from stud where sid=?",(sid,))
rows=cursor.fetchall()
print(rows)


sid= int(input(" enter your  id to delete\n :"))
cursor.execute("delete from stud where sid=?",(sid,))
conn.commit()
rows=cursor.fetchall()
print(rows)

update

sid=int(input("enter your id\n"))
cursor.execute("select * from stud where  sid=?",(sid,))
row=cursor.fetchone()
if sid==row[0]:
    new_name=input("enter  new name :")
    cursor.execute("update stud set name=? where sid=?",(new_name,sid))
    conn.commit()
    print("data updated!!")
else:
    print("no record found!!")    



