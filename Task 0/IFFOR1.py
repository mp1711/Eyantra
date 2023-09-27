'''
# Team ID:          cl_1054
# Theme:            Cosmo Logistic 
# Author List:      Hairsh BM, Vishwanath R, Sri Krishna R, Mukesh Prasanna
# Filename:         IFFOR1
# Functions:        sequence()
# Global variables: None
'''


# cook your dish here
def sequence(n):
    '''
    Purpose: to print the sequence as specified in question

    Input Arguments:
    ---
    n : integer

    Returns:
    ---
    None

    Example call:
    ---
    sequence(5)
    '''

    start = 1
    print(3, end=" ")
    while start < n-1:
        if start % 2 == 0:
            print(start*2, end=" ")
        else:
            print(start**2, end=" ")
        start += 1
    if n % 2 == 0:
        print(start**2)
    else:
        print(start*2)

    return


for _ in range(int(input())):
    n = int(input())
    if n == 0:
        continue

    sequence(n)
