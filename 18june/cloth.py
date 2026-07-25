from c import cloth
from g import grocery

c=cloth("clothes","Top",450,1,"violet","M")
g=grocery("Grocery","Sugar",80,"1kg","Madhur",'12-04-2026','11-04-2027')

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
            ip=int(input("what want to purchase 1.Grocery  2.Clothes:"))
            if ip==1:
                b=int(input("How much Quantity to buy:"))
                
                t=g.price*b
                l1.append([g.pro_name ,b,g.price ,t])
            elif ip==2:
                b=int(input("How much quantity to buy:"))
                t=c.price*b
                l1.append([c.pro_name,b,c.price,t])

            else:
                print("Invalid Choice")

            x=int(input("Do you want 1.Add more item 2.Generate Bill :"))
            if x==2:
                print("------Bill------")
                total=0
                print("proc\tqty\tprice\ttotal")
                for j in l1:
                    print( j[0],"\t",j[1],'\t',j[2],'\t',j[3])
                    total=total+j[3]
                print("Total Amount:",total)
                break   
        case 4:
            print("Thank You!!!")
            break;
        case _:
            print("Invalid Choice")