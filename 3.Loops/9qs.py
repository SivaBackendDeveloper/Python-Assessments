#Write a program to find the prime or not.

def prime(n):
    if n > 1:
        for i in range(2,n):
            if (n%i)==0:
                print(n,"is not prime")
                break
        else:
            print(n,"is prime")
    else:
        print(n,"is not a prime")

prime(13)