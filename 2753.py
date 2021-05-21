numbers = int(input())


if numbers % 4 ==0 and numbers % 100 !=0 or numbers % 400 ==0:
    print(1)

else:
    print(0)