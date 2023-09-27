'''
# Team ID:          cl_1054
# Theme:            Cosmo Logistic 
# Author List:      Hairsh BM, Vishwanath R, Sri Krishna R, Mukesh Prasanna
# Filename:         WLEN
# Functions:        None
# Global variables: None
'''

for _ in range(int(input())):
    sentence = input()[1:]
    # truncates the first character as [1:]
    words = sentence.split()
    word_lengths = []
    for word in words:
        word_lengths.append(str(len(word)))
    print(','.join(word_lengths))
