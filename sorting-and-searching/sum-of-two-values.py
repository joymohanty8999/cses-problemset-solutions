import sys

input = sys.stdin.readline
 
def solution(n, target, pair_arr):
    
    pair_arr.sort()
    
    l,r = 0, len(pair_arr) - 1
    
    while l < r:
        
        ele_sum = pair_arr[l][0] + pair_arr[r][0]
        
        if ele_sum == target:
            return (pair_arr[l][1],pair_arr[r][1])
        
        elif ele_sum > target:
            r -= 1
        
        else:
            l += 1
    
    return None
        

def main():
    
    n,target = map(int,input().split())
    arr = list(map(int,input().split()))
    
    pair_arr = list()
    
    for idx, ele in enumerate(arr):
        pair_arr.append((ele,idx + 1))
    
    result = solution(n,target,pair_arr)
    
    if result == None:
        print("IMPOSSIBLE")
    else:
        print(f"{result[0]} {result[1]}")
    
    
if __name__ == '__main__':
    main()