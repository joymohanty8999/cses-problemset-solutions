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

def solution(n: int, nums : List[int]) -> int:
    
    sum = (n*(n + 1)) // 2
    arr_sum = 0
    
    for num in nums:
        arr_sum += num
    
    return (sum - arr_sum)

def main():
    
    n = inp()
    nums = inlt()
    
    print(solution(n,nums))

    
if __name__ == '__main__':
    main()