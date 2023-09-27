'''
# Team ID:          cl_1054
# Theme:            Cosmo Logistic 
# Author List:      Hairsh BM, Vishwanath R, Sri Krishna R, Mukesh Prasanna
# Filename:         PAL
# Functions:        palindrome()
# Global variables: None
'''


def palindrome(pattern):
    '''
    Purpose: check whether the given string is palindrome or not

    Input Arguments:
    ---
    pattern : a pattern to check if it is a palindrome

    Returns:
    ---
    None

    Example call:
    ---
    palindrome('Aba')
    '''

    i, j = 0, len(pattern)-1
    pattern = pattern.lower()

    while i <= j:
        if pattern[i] != pattern[j]:
            print("It is not a palindrome")
            return
        i += 1
        j -= 1

    print("It is a palindrome")


for _ in range(int(input())):
    palindrome(input())
