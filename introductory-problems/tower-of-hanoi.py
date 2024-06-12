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

def count_moves(n : int) -> int:
    return (1 << n) - 1

def tower_of_hanoi(n : int , from_rod: chr, aux_rod : chr, to_rod: chr) -> int:
    
    if n == 0:
        return
    
    moves = tower_of_hanoi(n - 1, from_rod, to_rod, aux_rod)
    print(f"{from_rod} {to_rod}")
    moves = tower_of_hanoi(n - 1, aux_rod, from_rod, to_rod)

def solution(n : int):

    print(count_moves(n))
    tower_of_hanoi(n,'1','2','3')

    
def main():
    
   n = inp()
   solution(n)
    
if __name__ == '__main__':
    main()