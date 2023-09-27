'''
# Team ID:          cl_1054
# Theme:            Cosmo Logistic 
# Author List:      Hairsh BM, Vishwanath R, Sri Krishna R, Mukesh Prasanna
# Filename:         STAR
# Functions:        generate()
# Global variables: None
'''


def generate(n):
    '''
    Purpose: to print the star pattern as specified in question

    Input Arguments:
    ---
    n : integer
    number of lines in triangle

    Returns:
    ---
    None

    Example call:
    ---
    generate(5)
    '''

    stars = ["*"]*n
    for j in range(4, len(stars), 5):
        stars[j] = '#'
    pattern = ''.join(stars)
    while n > 0:
        print(pattern)
        pattern = pattern[:-1]
        n -= 1


for _ in range(int(input())):
    generate(int(input()))
