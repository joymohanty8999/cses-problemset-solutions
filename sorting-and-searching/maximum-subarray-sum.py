import sys
from typing import List

def maxSubarraySum(n : int, arr : List[int]) -> int:

    max_so_far, max_ending_here = -sys.maxsize - 1, 0

    for i in range(0, len(arr)):
        max_ending_here += arr[i]

        if max_ending_here > max_so_far:
            max_so_far = max_ending_here
        if max_ending_here < 0:
            max_ending_here = 0

    return max_so_far

def main():
    n = int(sys.stdin.readline())
    arr = list(map(int,sys.stdin.readline().split()))

    print(maxSubarraySum(n,arr))

if __name__ == "__main__":
    main()
