import sys
from typing import List, Dict

def MissingCoinSum(n : int, arr : List[int]) -> int:

    result = 1 # minimum sum
    arr.sort()

    for coin in arr:
        if coin > result:
            return result
        result += coin

    return result


def main():
    n = int(sys.stdin.readline())
    arr = list(map(int,sys.stdin.readline().split()))

    print(MissingCoinSum(n,arr))

if __name__ == "__main__":
    main()
