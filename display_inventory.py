""" Displaying inventory from a dictionary. """

stuff = { 'pillow': 12, 'torch': 4, 'rope': 5 }
my_list = ['pillow', 'line', 'line', 'blanket']

def display (inventory):
    print( 'Inventory: ' )
    total = 0
    for k,v in inventory.items():
        print (k + ': ' + str(v))
        total = total + v
    print ('Sum of items: ' + str(total))

def add_items (inventory, item_list):
    new_list = {}
    for i in item_list:
        if i not in inventory.keys():
            inventory [i] = 1
            #print (inventory)
        else:
            x = inventory[i]
            inventory[i] = x+1
    print(inventory)

add_items(stuff, my_list)
display(stuff)



