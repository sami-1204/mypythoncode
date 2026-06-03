num = 121
rev = 0
rem = 0
temp = num
while temp > 0:
    rem = temp % 10
    rev = rem + (rev*10)
    temp = temp // 10
    if (num == rev):
        print("its palindrome")
    else:
        print("its not palindrome")
