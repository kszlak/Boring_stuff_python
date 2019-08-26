"""Comma code."""

y = ['sleep', 'eat', 'smile', 'dance']

def mody_list(x):
    """Take a list and print as a string with commas and 'and' before the last word ."""
    i = 0
    new = ''
    while i < len(x)-2:
        new = (new + str(x[i]) + ', ')
        i = i + 1
    new = (new + str(x[-2]) + ' and ' + str(x[-1]))
    return new

print(mody_list(y))