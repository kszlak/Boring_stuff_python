"""Asking for age."""

print('Hi')
while True:
    print('Who are you?')
    name = input()
    if name != ('Lil'):
        continue
    print ('Hi Lil, please enter pass: ')
    passwd = input()
    if passwd == ('jellyfish'):
        break

print ('Access granted Lil, enjoy!')
print()
print('The length of your name is: ')
print(len(name))

print('What is your age?') #ask for age
age=input()
print('Your age is ')
print('You will be ' + str(int(age)+1) + ' in a year.') #tell you age in a year

oks = ''
while oks != 'OK':
    print('Was it funny? Say OK ;)')
    oks = input()

print ('Thank you!')