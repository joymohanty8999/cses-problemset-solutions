import sys
from typing import List

class Graph:
    
    def __init__(self, rows: int, cols: int, g: List[List[str]]):
        self.rows = rows
        self.cols = cols
        self.graph = g
    
    def dfs(self, start_i: int, start_j: int, visited: List[List[bool]]):
        
        # implementing iterative solution to tackle TLE
        
        stack = [(start_i,start_j)]
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        
        while stack:
            
            i,j = stack.pop()
        
            if (i < 0 or i >= self.rows) or (j < 0 or j >= self.cols) or visited[i][j] or self.graph[i][j] == '#':
                continue
            
            visited[i][j] = True
            
            for di, dj in directions:
                new_i, new_j = i + di, j + dj
                
                if 0 <= new_i < self.rows and 0 <= new_j < self.cols and not visited[new_i][new_j] and self.graph[new_i][new_j] == '.':
                    stack.append((new_i, new_j))
    
    def countRooms(self) -> int:
    
        visited = [[False for j in range(self.cols)] for i in range(self.rows)]
        count = 0
        
        for i in range(self.rows):
            for j in range(self.cols):
                if not visited[i][j] and self.graph[i][j] == '.':
                    self.dfs(i,j, visited)
                    count += 1
        
        return count

def main():
    n,m = map(int, sys.stdin.readline().split())
    
    graph = []
    
    for line in sys.stdin.readlines():
        line = line.strip()
        graph.append(list(line))
        
    g = Graph(n, m, graph)
    print(g.countRooms())

if __name__ == "__main__":
    main()