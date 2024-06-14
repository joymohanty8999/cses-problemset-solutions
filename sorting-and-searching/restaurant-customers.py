import sys
from typing import List
 
def solution(n : int, in_times : List[int], out_times : List[int]):
    
    in_times.sort()
    out_times.sort()
    
    max_customers,curr_customers,in_idx, out_idx = 0,0,0,0
    
    while in_idx < n and out_idx < n:
        
        if in_times[in_idx] <= out_times[out_idx]:
            curr_customers += 1
            in_idx += 1
        
        else:
            curr_customers -= 1
            out_idx += 1
            
        max_customers = max(max_customers, curr_customers)
        
    print(max_customers)
    

def main():
    
    n = int(sys.stdin.readline())
    in_times, out_times = list(), list()
    
    for i in range(0,n):
        a,b = map(int,sys.stdin.readline().split())
        in_times.append(a)
        out_times.append(b)
        
    solution(n, in_times, out_times)
    
if __name__ == '__main__':
    main()