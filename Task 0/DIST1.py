'''
# Team ID:          cl_1054
# Theme:            Cosmo Logistic 
# Author List:      Hairsh BM, Vishwanath R, Sri Krishna R, Mukesh Prasanna
# Filename:         DIST1
# Functions:        compute_distance()
# Global variables: None
'''


import math


def compute_distance(x1, y1, x2, y2):
    '''
    Purpose: calc distance between 2 points

    Input Arguments:
    ---
    x1, x2 : integers
    coordinates of x-axis of start and finish points respectively

    y1, y2 : integers
    coordinates of y-axis of start and finish points respectively

    Returns:
    ---
    floating point distance between 2 points

    Example call:
    ---
    compute_distance(5,1,2,3)
    '''

    dist = math.sqrt((x1-x2)**2 + (y1-y2)**2)
    return dist


test_cases = int(input())
for i in range(test_cases):
    x1, y1, x2, y2 = map(int, input().split())
    val = compute_distance(x1, y1, x2, y2)
    f_val = '{:.2f}'.format(val)
    # f_val is formatted value
    print(f"Distance: {f_val}")
