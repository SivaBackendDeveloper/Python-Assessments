#Write a program to create your own exception

try:
    1 / 0

except Exception as err:
    # perform any action on Exception instance
    print("Error:", err)


