#. Write a program with finally block

try:
    k = 5 // 0  # exception raised
    print(k)

finally:
    # this block is always executed
    # regardless of exception generation.
    print('This is always executed')

# or

try:
    k = 5 // 0  # exception raised
    print(k)

except ZeroDivisionError:
    print("number not divisable by zero")

finally:
    # this block is always executed
    # regardless of exception generation.
    print('This is always executed')

