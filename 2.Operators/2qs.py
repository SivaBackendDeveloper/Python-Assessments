#Write a method for increment and decrement 2.Operators(++, --)

def increment():
    cnt = 0
    cnt += 1
    cnt = cnt + 1
    print('The Value of Count is', cnt)

    # unlike many other languages, it doesn't use ++
    # this is for increment operator here start = 1,
    # stop = 5 and step = 1(by default)
    print("INCREMENTED FOR LOOP")
    for i in range(0, 10):
        print(i)

def decrement():
    cnt = 0
    cnt += 1
    cnt = cnt + 1
    print('The Value of Count is', cnt)
    # this is for increment operator here start = 5,
    # stop = -1 and step = -1
    print("\n DECREMENTED FOR LOOP")
    for i in range(9, -1, -1):
        print(i)

increment()
decrement()