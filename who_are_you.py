""" Who are you code. """

name = ''
while name != 'Lil':
    print ('Who are you?')
    name = input()
    if name == ('Lil'):
        print ('Hi Lil')

passwd = ''
while passwd != 'jellyfish':
    print('Enter your fish password please')
    passwd = input()
    if passwd == 'jellyfish':
        print('Hello, enjoy!')
    break

print ('Your name is ' + name)
for i in range (5):
    print (name + ' ' +str(i))

#adding numbers from 0 to 100
sum = 0
for num in range (101):
    sum = sum + num
print (sum)