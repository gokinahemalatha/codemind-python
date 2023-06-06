from itertools import permutations
def allp(s):
    l=permutations(s)
    for i in list(l):
        print(''.join(i))
s=input()
allp(s)