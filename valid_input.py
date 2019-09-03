while True:
    ask = (' Write your age: ')
    answear_age = input()
    if answear_age.isdecimal():
        return (' Great, thank you! ')
    else:
        print(' Please enter your age, I know you did not ;) ')

while True:
    passwd = input()
    if passwd.isalnum():
        break
    else:
        print( ' Password should contain only letters and numbers. ' )
