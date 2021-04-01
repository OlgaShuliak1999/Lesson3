from random import randint

x = int(input("Enter the Number from 1 to 10 = "))
n = randint(1,10)
i = 1
while  i < 3:
    print(i,"you have more tries")
    if x == n:
        print(f' {i} You won')
    elif x != n:
        x = int(input("Try again = "))
    i +=1
else:
    print(f' {i}  You lose')



