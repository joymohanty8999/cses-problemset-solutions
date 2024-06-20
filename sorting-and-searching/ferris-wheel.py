
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

def solution(p : List[int], x : int) -> int:

    p.sort()
    gondolas = 0

    # remove all the weights == x and add one gondola to it

    l = list()

    for ps in p:

        if ps < x:
            l.append(ps)

        elif ps == x:
            gondolas += 1

    #print(l)

    left, right = 0, len(l) - 1

    while left <= right:

        if p[left] + p[right] > x:
            gondolas += 1
            right = right - 1
        else:
            gondolas += 1
            left = left + 1
            right = right - 1

    return gondolas

def main():

    n,x = invr()
    p = inlt()

    print(solution(p,x))

if __name__ == '__main__':
    main()
