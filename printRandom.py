import random
import sys

for i in range(5):
    print (random.randint(1,10))
    print("More?")
    ex = input()
    if ex == ("no"):
        sys.exit()
