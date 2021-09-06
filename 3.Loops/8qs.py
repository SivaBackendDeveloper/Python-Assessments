#Write a program to find Armstrong number or not

def armstrong(n):
    i = n
    sum = 0
    while n != 0:
        rem = n % 10
        s = rem ** 3
        sum = sum + s
        n = n // 10
    if i == sum:
        print(i, "is a armstrong number")
    else:
        print(i, "is not armstrong number")

armstrong(153)