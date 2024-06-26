import sys
from typing import List, Dict

def minTotalCost(n : int, arr : List[int]):

    if n == 1:
        return 0

    elif n == 2:
        return abs(arr[0] - arr[1])

    arr.sort()

    mid = len(arr) // 2
    sum = 0

    for i in range(0,len(arr)):
        sum += abs(arr[mid] - arr[i])

    return sum

def main():
    n = int(sys.stdin.readline())
    arr = list(map(int,sys.stdin.readline().split()))

    print(minTotalCost(n,arr))

if __name__ == "__main__":
    main()
