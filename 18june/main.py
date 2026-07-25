from c import cloth
from g import grocery

c=cloth("clothes","Top",450,1,"violet","M")
g=grocery("Grocery","Sugar",80,"1","Madhur",'12-04-2026','11-04-2027')

l1=[]
while True:
    print("Welcome to Dmart\n1.Grocery Section \n2.Clothing Section \n3.Purchase \n4.Exit")
    ch=int(input("Enter your Choice:"))
    match ch:
        case 1:
            print(g.show())
        case 2:
            print(c.dis())
        case 3:
            while True:
                ip=int(input("what want to purchase 1.Grocery 2.Clothes :"))

                if ip==1:
                    a=int(input("How much quantity to add:"))
                    t=g.price*a
                    l1.append([g.pro_name,g.price,a,t])

                elif ip==2:
                    a=int(input("How much quantity to add:"))
                    t=c.price*a
                    l1.append([c.pro_name,c.price,a,t])

                print(l1)

                ask=int(input("What do you want to 1.add more items 2.Generate bill:"))
                if ask==1:
                    continue
                elif ask==2:
                    print("-----Bill-----")
                    print("proc\tprice\tqty\ttotal")
                    total=0

                    for i in l1:
                        print(i[0],"\t",i[1],"\t",i[2],"\t",i[3])
                        total += i[3]

                    print("Total Amount:", total)
                    break;
           
         
        case 4:
            print("Thank You!!!")
            break;
        case _:
            print("Invalid Choice")