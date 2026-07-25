x = ((20,40,50), 20, 50, ["hello","bye"])

print("Tuple Elements:")
for i in x:
    if type(i) == tuple:
        for item in i:
            print(item)

print("\nList Elements:")
for i in x:
    if type(i) == list:
        for item in i:
            print(item)
