while True:
    ask = (' Write your age: ')
    answear_age = input()
    if answear_age.isdecimal():
        break
    print(' Please enter your age, I know you did not ;) ')

while True:
    passwd = input()
    if passwd.isalnum():
        break
    print( ' Password should contain only letters and numbers. ' )
