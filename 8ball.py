import random

get_answer = ['For sure!', 'Never', 'Why not', 'Forget about it',
              'Concentrate and ask again', 'Be wise', 'Lets do it',
              'No. I said No.', 'Seriously?', 'Yes. Do it right now!']

print(get_answer[random.randint(0, len(get_answer) - 1)])