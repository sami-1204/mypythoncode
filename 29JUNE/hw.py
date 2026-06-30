import sqlite3

conn=sqlite3.connect("student.db")

cursor=conn.cursor()

cursor.execute('''
    create table if not exists student(
                rollno INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                sub1 INTEGER,
                sub2 INTEGER,
                sub3 INTEGER
    )
''')
conn.commit()


while True:


    print("1. Add Student 2. Update Marks = 0 3. Update Multiple Information 4. Update Particular Field 5. View Student 6. Search Student 7. Delete Student 8. View Result 9. Exit")

    ch = int(input("Enter choice: "))


    match(ch):
        case 1:
                rollno = int(input("Enter Roll No: "))
                name = input("Enter Name: ")
                sub1 = int(input("Enter Subject1 Marks: "))
                sub2 = int(input("Enter Subject2 Marks: "))
                sub3 = int(input("Enter Subject3 Marks: "))

                cursor.execute("INSERT INTO student VALUES(?,?,?,?,?)",(rollno, name, sub1, sub2, sub3))

                conn.commit()
                print("Student Added Successfully")
        
        
        #UPDATE MARKS TO 0
        case 2:
                rollno = int(input("Enter Roll No: "))

                cursor.execute("UPDATE student SET sub1=0, sub2=0, sub3=0 WHERE rollno=?",(rollno,))

                conn.commit()
                print("Marks Updated to 0")

            
            #UPDATE MULTIPLE
        case 3:
                
                rollno = int(input("Enter Roll No: "))

                name = input("Enter New Name: ")
                sub1 = int(input("Enter New Subject1 Marks: "))
                sub2 = int(input("Enter New Subject2 Marks: "))
                sub3 = int(input("Enter New Subject3 Marks: "))

                cursor.execute("UPDATE student SET name=?, sub1=?, sub2=?, sub3=? WHERE rollno=?", (name, sub1, sub2, sub3, rollno))

                conn.commit()
                print("Information Updated")

        # Update particular field
        case 4:
            rollno = int(input("Enter Roll No: "))
            field = input("Enter field(name/sub1/sub2/sub3): ")
            value = input("Enter new value: ")

            query = f"UPDATE student SET {field}=? WHERE rollno=?"

            cursor.execute(query, (value, rollno))
            conn.commit()

            print("Field Updated")

        # View
        case 5:

            print("1. View By Roll No")
            print("2. View All")

            op = int(input("Enter choice: "))

            if op == 1:
                rollno = int(input("Enter Roll No: "))

                cursor.execute(
                    "SELECT * FROM student WHERE rollno=?",
                    (rollno,)
                )

                rowno = cursor.fetchone()

                if rowno:
                    print(rowno)
                else:
                    print("Record Not Found")

            else:
                cursor.execute("SELECT * FROM student")

                rows = cursor.fetchall()

                for r in rows:
                    print(r)

        # Search
        case 6:

            print("""
            1. Search By Roll No
            2. Search By Name
            3. Search By Marks
            """)

            op = int(input("Enter choice: "))

            if op == 1:
                rollno = int(input("Enter Roll No: "))

                cursor.execute("SELECT * FROM student WHERE rollno=?",(rollno,))

            elif op == 2:
                name = input("Enter Name: ")

                cursor.execute("SELECT * FROM student WHERE name=?",(name,))

            elif op == 3:
                marks = int(input("Enter Marks: "))

                cursor.execute("SELECT * FROM student WHERE sub1=? OR sub2=? OR sub3=?", (marks, marks, marks))

            rows = cursor.fetchall()

            if rows:
                for r in rows:
                    print(r)
            else:
                print("No Record Found")

        # Delete
        case 7:

            print("1. Delete One")
            print("2. Delete All")

            op = int(input("Enter choice: "))

            if op == 1:
                rollno = int(input("Enter Roll No: "))

                cursor.execute("DELETE FROM student WHERE rollno=?",(rollno,))

            else:
                cursor.execute("DELETE FROM student")

            conn.commit()
            print("Deleted Successfully")

        # View Result
        case 8:

            rollno = int(input("Enter Roll No: "))

            cursor.execute("SELECT * FROM student WHERE rollno=?",(rollno,))

            row = cursor.fetchone()

            if row:

                total = row[2] + row[3] + row[4]
                percentage = total / 3

                print("\n------ MARKSHEET ------")
                print("Roll No :", row[0])
                print("Name :", row[1])
                print("Subject1 :", row[2])
                print("Subject2 :", row[3])
                print("Subject3 :", row[4])
                print("Total :", total)
                print("Percentage :", round(percentage, 2), "%")

            else:
                print("Record Not Found")

        case 9:
            print("Thank You")
            break
        
        case _:
            print("Invalid Choice")
            break
