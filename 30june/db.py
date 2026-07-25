import mysql.connector

#creating connection
conn=mysql.connector.connect(host="localhost",
                             user="root",
                             password="samuu@124",
                             database="linkcode")
print("database created")

cursor=conn.cursor()
#create table
cursor.execute('''
                create table if not exists emp(
                    empid int primary key auto_increment,
                    name varchar(20) not null,
                    salary decimal(10,2) check(salary>0)
                )
               ''')
conn.commit()
print("table created")

               