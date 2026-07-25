import mysql.connector

conn = mysql.connector.connect(
    host  = "localhost",
    username = "root",
    password = "samuu@124",
    database = "sms_linkcode"
)

print("db connected!")

cursor = conn.cursor()

# cursor.execute("create table resume(id int primary key auto_increment,fullname varchar(30),position varchar(30),resume LONGBLOB)")
# print("table is created!")

print("1.Uplaod Resume\n2.Read Resume\n3.Update Resume\n4.Delete Resume")

choice = int(input("enter your choice!"))

match choice:

    case 1:

        print("============ Upload Resume ========== ")

        name = input("enter name :")
        
        position = input("enter position :")
        path = input("enter resume path :")

        with open(path,"rb") as file:
                 pdf = file.read()

                 query = ("insert into resume(fullname,position,resume) values(%s,%s,%s)")
                 values = (name , position , pdf)

                 cursor.execute(query,values)
                 conn.commit()
                 print("resume uploaded successfully")
    
    case 2:
          
              print("============ Read Resume ========== ")

              id = int(input("Enter ID: "))

              sql = "SELECT resume FROM resume WHERE id=%s"
              cursor.execute(sql, (id,))

              record = cursor.fetchone()
              if record:
                   with open("download_resume.pdf", "wb") as file:
                    file.write(record[0])
                    print("Resume Downloaded")
              else:
                    print("Record Not Found")
    case 3:
          print("============ Upadte name in  Resume ========== ")
          
          old_name = input("Enter Existing Name: ")
          new_name = input("Enter New Name: ")

          query = "UPDATE resume SET fullname = %s WHERE fullname = %s"
          values = (new_name, old_name)

          cursor.execute(query, values)
          conn.commit()

          if cursor.rowcount > 0:
               print("Name Updated Successfully")
          else:
                 print("Record Not Found")
# cursor.close()
# conn.close()
    
    case 4:
            print("============ Delete Resume ========== ")

            id = int(input("Enter ID: "))

            sql = "DELETE FROM resume WHERE id=%s"

            cursor.execute(sql, (id,))
            conn.commit()

            print("Resume Deleted")
