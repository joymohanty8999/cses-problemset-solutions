import sys
from typing import List, Dict

def CollectingNumbers(n : int, arr : List[int]):

    passes = 1
    idxs = [0] * (n + 1)

    for i in range(n):
        idxs[arr[i]] = i

    for num in range(1,n):
        if idxs[num + 1] < idxs[num]:
            passes += 1

    return passes



def main():
    n = int(sys.stdin.readline())
    arr = list(map(int,sys.stdin.readline().split()))

    print(CollectingNumbers(n,arr))

if __name__ == "__main__":
    main()
