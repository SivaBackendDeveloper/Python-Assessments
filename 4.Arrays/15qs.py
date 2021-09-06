#15. Write a method to find number of even number and odd numbers in an array

def evenOdd(numbers):
    even = []
    odd = []
    for number in numbers:
        if int(number) % 2 == 0:
            even.append(number)
        else:
            odd.append(number)
    return even, odd


if __name__ == '__main__':
    Input = input("Enter the numbers (space separated) to check: ")
    Input = list(Input.split())
    even, odd = evenOdd(Input)
    print('Even Nos: ', ','.join(even), '\n', 'Odd Nos: ', ','.join(odd))