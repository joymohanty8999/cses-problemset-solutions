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

def solution(n : int, arr : List[int]) -> int:

    if n == 0:
        return 0
    
    arr.sort()
    distinct_cnt = 1
    
    for i in range(1, n):
        if arr[i] != arr[i - 1]:
            distinct_cnt += 1
    
    return distinct_cnt
    
def main():
    
   n = inp()
   arr = inlt()
   
   print(solution(n, arr))
    
if __name__ == '__main__':
    main()