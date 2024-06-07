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

def solution(y : int, x : int):
    
    if y > x:
        
        result = (y - 1) * (y - 1)
        
        if y % 2 != 0:
            result += x
        else:
            result += (2*y - x)
        
        return result
    
    else:
        
        result = (x - 1) * (x - 1)
        
        if x % 2 == 0:
            result += y
        else:
            result += (2*x - y)
            
        return result
    
    

def main():
    
   t = inp()
   
   for i in range(0,t):
       y,x = invr()
       print(solution(y,x))

    
if __name__ == '__main__':
    main()