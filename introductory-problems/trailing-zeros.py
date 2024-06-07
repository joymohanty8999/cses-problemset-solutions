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

def solution(n : int):
    
    cnt = 0
    power_of_5 = 5
    
    while n >= power_of_5:
        
        cnt += n // power_of_5
        power_of_5 *= 5
        
        
    print(cnt)
    
    

def main():
    
   n = inp()
   solution(n)
    
if __name__ == '__main__':
    main()