# file = open("img.jpg","rb")
# data = file.read()
# print(data)
# file.close()

# with open("copy_img.jpg","wb") as file:
#     file.write(data)

import mysql.connector

conn = mysql.connector.connect(
    host  = "localhost",
    username = "root",
    password = "samuu@124",
    database = "sms_linkcode"
)

print("db connected!")

cursor = conn.cursor()

# cursor.execute("create table files(id int primary key auto_increment,filename varchar(20),filedata LONGBLOB)")
# print("table is created!")

#read binary data

# file = open("img.jpg","rb")
# data = file.read()
# print(data)
# file.close()

# query = "insert into files(filename,filedata) values(%s,%s)"
# values = ("img.jpg",data)
# cursor.execute(query,values)
# conn.commit()
# print("save data!")

#fetch

cursor.execute("select * from files where id=%s",(1,))
record=cursor.fetchone()
if record:
    filename=record[1]
    filedata=record[2]

    #save to sys

    file=open(filename,"wb")
    file.write(filedata)
    file.close()
    print("downloaded....")
else:
    print("record not found")

cursor.close()
conn.close()