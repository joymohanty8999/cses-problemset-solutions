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
    
    total_sum = (n*(n + 1)) // 2
    
    if total_sum % 2 == 0:
        print("YES")
        
        target, idx = total_sum // 2, 0
        arr = [n - i + 1 for i in range(1, n + 1)]
        
        l1 = list()
        
        while target != 0 and idx < len(arr):
            
            if target - arr[idx] >= 0:
                l1.append(arr[idx])
                target -= arr[idx]
            
            idx += 1
            
        set1= set(l1) 
        l2 = [num for num in arr if num not in set1]
        
        print(len(l1))
        print(*l1)
        
        print(len(l2))
        print(*l2)
        
    
    else:
        print("NO")
    
    

def main():
    
   n = inp()
   solution(n)

    
if __name__ == '__main__':
    main()