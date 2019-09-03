""" Displaying inventory from a dictionary after adding some new stuff form  the list. """

stuff = { 'pillow': 12, 'torch': 4, 'rope': 5 }
my_list = ['pillow', 'line', 'line', 'blanket']


def display (inventory):
    """ Display inventory """
    print( '\nInventory: \n' )
    total = 0
    for k,v in inventory.items():
        print (k + ': ' + str(v))
        total = total + v
    print ('\nSum of items: ' + str(total))

def add_items (inventory, item_list):
    """ Add item_list to inventory dictionary """
    new_list = {}
    for i in item_list:
        if i not in inventory.keys():
            inventory [i] = 1
        else:
            x = inventory[i]
            inventory[i] = x+1


add_items(stuff, my_list)
display(stuff)