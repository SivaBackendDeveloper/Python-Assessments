#Write a program to palindrome or not.

def palindrome(n):
    i = n
    rev = 0
    while n != 0:
        rem = n % 10
        rev = (rev * 10) + rem
        n = n // 10
    if rev == i:
        print(i, "is palindrome number")
    else:
        print(i, "is not a palindrome")

palindrome(131)
