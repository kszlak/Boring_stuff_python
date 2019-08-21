# This program says hi and ask for my age

print('Hi')
print('What is your name?')  # ask for name
name = input()

print('Really nice to meet you ' + name)
print('The length of your name is: ')
print(len(name))

print('What is your age?') #ask for age
age=input()
print('Your age is ')
print('You will be ' + str(int(age)+1) + ' in a year.')