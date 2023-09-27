'''
# Team ID:          cl_1054
# Theme:            Cosmo Logistic 
# Author List:      Hairsh BM, Vishwanath R, Sri Krishna R, Mukesh Prasanna
# Filename:         SCOR
# Functions:        None
# Global variables: None
'''

for _ in range(int(input())):

    n = int(input())
    toppers = []
    max_mark = 0

    for i in range(n):
        name, mark = input().split()
        if max_mark < float(mark):
            toppers.clear()
            toppers.append(name)
            max_mark = float(mark)
        elif max_mark == float(mark):
            toppers.append(name)

    toppers.sort()
    for name in toppers:
        print(name)
