'''
# Team ID:          cl_1054
# Theme:            Cosmo Logistic 
# Author List:      Hairsh BM, Vishwanath R, Sri Krishna R, Mukesh Prasanna
# Filename:         INV_PY
# Functions:        add(), delete()
# Global variables: None
'''


def add(item, qty):
    '''
    Purpose: Add an item into the inventory

    Input Arguments:
    ---
    item :  string
    a string representing the item to add into the inventory

    qty : integer
    an integer signfying the quantity to add for the particular item specified

    Returns:
    ---
    a string with item and the respective message as specified in question

    Example call:
    ---
    add('Servo', 5)
    '''

    if item in inventory:
        inventory[item] += qty
        return "UPDATED Item " + item
    else:
        inventory[item] = qty
        return "ADDED Item " + item


def delete(item, qty):
    '''
    Purpose: Delete an item from the inventory

    Input Arguments:
    ---
    item :  string
    a string representing the item to add into the inventory

    qty : integer
    an integer signfying the quantity to deleteif particular item specified is in the inventory directory

    Returns:
    ---
    a string with item and the respective message as specified in question

    Example call:
    ---
    delete('Servo', 5)
    '''
    if item not in inventory:
        return "Item " + item + " does not exist"
    else:
        if qty > inventory[item]:
            return "Item " + item + " could not be DELETED"
        else:
            inventory[item] -= qty
            return 'DELETED Item ' + item


for _ in range(int(input())):
    inventory = {}
    N = int(input())
    for i in range(N):
        item, qty = input().split()
        inventory[item] = int(qty)
    M = int(input())
    for i in range(M):
        operation, item, qty = input().split()
        qty = int(qty)
        if operation == "ADD":
            print(add(item, qty))
        else:
            print(delete(item, qty))

    print("Total Items in Inventory:", sum(inventory.values()))
