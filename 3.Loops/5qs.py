#Write a program to print largest number among three numbers.

def greatest(a,b,c):
    while True:
        if a>b and a>c:
            print(a,"is larger than three numbers")
            break
        elif b>c:
            print(b,"is larger than three numbers")
            break
        else:
            print(c,"is larger than three numbers")
            break

greatest(30,200,10)