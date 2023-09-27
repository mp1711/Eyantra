'''
# Team ID:          cl_1054
# Theme:            Cosmo Logistic 
# Author List:      Hairsh BM, Vishwanath R, Sri Krishna R, Mukesh Prasanna
# Filename:         D2BIN1
# Functions:        dec_to_binary()
# Global variables: None
'''


def dec_to_binary(n):
    '''
    Purpose: Convert a decimal to binary number

    Input Arguments:
    ---
    n : decimal number
    input number to convert to binary

    Returns:
    ---
    a binary number of string data type

    Example call:
    ---
    dec_to_binary(5)
    '''

    bin_num = ""
    while n > 0:
        bin_num = str(n % 2)+bin_num
        n //= 2

    bin_num = "0"*(8-len(bin_num))+bin_num
    # append leading zeros
    return bin_num


# Main function
if __name__ == '__main__':
    for case in range(int(input())):
        n = int(input())
        bin_num = dec_to_binary(n)
        print(bin_num)
