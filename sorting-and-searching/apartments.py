import sys
from typing import List, Dict

input = sys.stdin.readline

############ ---- Input Functions ---- ############
def inp():
    return(int(input()))
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s)]))
def invr():
    return(map(int,input().split()))
####################################################

def solution(a : List[int],b : List[int], k : int) -> int:

    a.sort()
    b.sort()
    matches = 0
    
    i,j = 0,0
    
    while i < len(a) and j < len(b):
        
        # too small apt go to next apartment
        if b[j] < a[i] - k:
            j += 1
            
        # too big apt go to next applicant
        elif b[j] > a[i] + k:
            i += 1
            
        # match
        else:
            matches += 1
            i += 1
            j += 1
            
    return matches
    
def main():
    
    n,m,k = invr()
    a = inlt()
    b = inlt()
    
    print(solution(a,b,k))
    
if __name__ == '__main__':
    main()