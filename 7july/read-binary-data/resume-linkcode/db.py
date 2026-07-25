import mysql.connector

def connection():
    conn = mysql.connector.connect(
    host  = "localhost",
    username = "root",
    password = "samuu@124",
    database = "sms_linkcode"
)

print("db connected!")


