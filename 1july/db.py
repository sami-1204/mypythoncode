import mysql.connector

# 1. Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",       
    password="samuu@124", 
    database="linkcode" 
)

cursor = conn.cursor()

# 2. Create table
cursor.execute("""
    create table if not exists emp(
        empid int primary key auto_increment,
        name varchar(20) not null,
        sal decimal(10,2) check(sal>0)
    )
""")

conn.commit()
print("table created")
