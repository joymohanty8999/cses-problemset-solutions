import sys
from typing import List

input = sys.stdin.readline

############ ---- Input Functions ---- ############
def inp():
    return(int(input()))
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s) - 1]))
def invr():
    return(map(int,input().split()))
####################################################

def printlist(l : List):
    
    for ele in l:
        print(f"{ele}", end = " ")

def solution(n : int) -> List[int]:
    
    result = list()
    
    while n != 1:
        
        result.append(n)
        
        if n % 2 == 0:
            n //= 2
        else:
            n = (n*3) + 1
            
    result.append(1)
            
    return result
        

def main():
    
    n = inp()
    result = solution(n)
    
    printlist(result)    
    
if __name__ == '__main__':
    main()