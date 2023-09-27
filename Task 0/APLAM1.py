'''
# Team ID:          cl_1054
# Theme:            Cosmo Logistic 
# Author List:      Hairsh BM, Vishwanath R, Sri Krishna R, Mukesh Prasanna
# Filename:         APLAM1
# Functions:        generate_AP()
# Global variables: None
'''


def generate_AP(a1, d, n):
    '''
    Purpose: to return a list of n terms of AP in the form of list

    Input Arguments:
    ---
    a1 :  integer
    first element of AP

    d : common difference
    difference between any 2 consecutive elements

    n : number of terms

    Returns:
    ---
    list with n terms of AP

    Example call:
    ---
    generate_AP(5, 5, 7)
    '''

    if n == 0:
        return

    AP_series = [a1]
    for i in range(n-1):
        AP_series.append(a1+d)
        a1 += d

    return AP_series


# Main function
if __name__ == '__main__':

    for _ in range(int(input())):

        a1, d, n = map(int, input().split())
        # a1 first element, d difference, n number of terms

        AP_series = generate_AP(a1, d, n)
        sqr_AP_series = [i**2 for i in AP_series]
        sum_sqr_AP_series = sum(sqr_AP_series)
        print(*AP_series)
        print(*sqr_AP_series)
        # print(*l) prints a sequence of space seperated elements
        print(sum_sqr_AP_series)
