'''
# Team ID:          cl_1054
# Theme:            Cosmo Logistic 
# Author List:      Hairsh BM, Vishwanath R, Sri Krishna R, Mukesh Prasanna
# Filename:         SLICE1
# Functions:        None
# Global variables: None
'''


for _ in range(int(input())):
    length = int(input())
    nums = list(map(int, input().split()))
    print(*nums[::-1])
    # nums[::-1] reverses the list
    nums3, nums5 = [], []
    for i in range(3, length, 3):
        nums3.append(l[i]+3)
    for i in range(5, length, 5):
        nums5.append(l[i]-7)
    print(*nums3)
    print(*nums5)
    print(sum(nums[3:8]))
