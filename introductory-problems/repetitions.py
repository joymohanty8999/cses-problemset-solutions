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

def printlist(l : List):
    
    for ele in l:
        print(f"{ele}", end = " ")

def solution(seq : List[chr]) -> int:
    
    if len(seq) == 1:
        return 1
    
    max_len, curr_len = 1,1
    prev_ch = seq[0]
    
    for i in range(1, len(seq)):

        # current character is equal to previous character
        if seq[i] == prev_ch:
            curr_len += 1
            
        else:
            max_len = max(max_len, curr_len)
            curr_len = 1
            
        #print(f"{max_len},{curr_len},{prev_ch},{seq[i]},{i}")
            
        prev_ch = seq[i] # update previous character
        
    max_len = max(max_len, curr_len)
    
    return max_len
    

def main():
    
    sequence = insr()
    #print(sequence)
    print(solution(sequence))

    
if __name__ == '__main__':
    main()