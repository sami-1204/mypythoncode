from db import connection

def upload():
    path = input("enter yourn path to upload resume\n")
    file = open(path,"rb")
    data = file.read()
    file.close()

    filename = path.split("\\")[-1]
    extension = file.split('.')[-1]

    conn=connection()
    cursor=conn.cursor()

    query = ("insert to files ")