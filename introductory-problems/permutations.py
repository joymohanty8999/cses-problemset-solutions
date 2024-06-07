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
    return(list(s[:len(s)]))
def invr():
    return(map(int,input().split()))
####################################################

def solution(n : int) -> List[int] | None:
    
    if n == 2 or n == 3:
        return None
    
    even = []
    odd = []
    
    for i in range(1, n + 1):
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
            
    return (even + odd)
    

def main():
    
    n = inp()
    
    result = solution(n)
    
    if result == None:
        print("NO SOLUTION")
    
    else:
        print(*result)

    
if __name__ == '__main__':
    main()