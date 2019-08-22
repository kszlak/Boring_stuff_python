import random

def get_answer(number):
    if number == 1:
        return 'For sure!'
    if number == 2:
        return 'Never'
    if number == 3:
        return 'Why not'
    if number == 4:
        return 'Forget about it'
    if number == 5:
        return 'Concentrate and ask again'
    if number == 6:
        return 'Be wise'
    if number == 7:
        return 'Lets do it'
    if number == 8:
        return 'No. I said No.'
    if number == 9:
        return 'Seriously?'
    if number == 10:
        return 'Yes. Do it right now!'

r = random.randint(1,10)
fortune = get_answer(r)
print (fortune)