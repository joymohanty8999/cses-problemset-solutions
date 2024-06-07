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

def solution(arr : List[int]):
    
    moves = 0
    
    for i in range(1, len(arr)):
        if arr[i] < arr[i - 1]:
            moves += (arr[i - 1] - arr[i])
            arr[i] = arr[i - 1] 
    
    return moves
    
    

def main():
    
    n = inp()
    arr = inlt()
    
    print(solution(arr))

    
if __name__ == '__main__':
    main()