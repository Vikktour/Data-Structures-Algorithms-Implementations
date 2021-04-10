"""
Victor Zheng
04-10-2021
329. Longest Increasing Path in a Matrix (Hard)
""" 
from typing import List 
"""
Approach 1.1: TLE O(M*N*3^(M*N-1)) runtime O(M*N) space - where M=#rows, N=#cols
DFS
"""

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        M = len(matrix)
        N = len(matrix[0])
        self.maxLength = 0
        visited = set()
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        
        def dfs(x,y,depth):
            
            if depth > self.maxLength:
                self.maxLength = depth
            
            for dx,dy in directions:
                nx,ny = x+dx,y+dy
                if 0<=nx<M and 0<=ny<N and (nx,ny) not in visited and matrix[x][y] < matrix[nx][ny]:
                    visited.add((nx,ny))
                    dfs(nx,ny,depth+1)
                    visited.remove((nx,ny)) #backtrack
        
        for i in range(M):
            for j in range(N):
                dfs(i,j,1)
        return self.maxLength
"""
Approach 1.2: O(M*N) runtime O(M*N) space - 436ms(80.95%),14.9MB(87.80%)
DFS with memoization
Note that we no longer need visited because checking neighbors is O(4) which is fast and won't have recursion if they are reached once already
"""

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        M = len(matrix)
        N = len(matrix[0])
        self.maxLength = 0
        #visited = set()
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        
        memo = [[-1]*N for _ in range(M)]
        #print(memo)
        
        def dfs(x,y):
            if memo[x][y] != -1:
                return memo[x][y]
            bestNeighborDepth = 0
            for dx,dy in directions:
                nx,ny = x+dx,y+dy
                #if 0<=nx<M and 0<=ny<N and (nx,ny) not in visited and matrix[x][y] < matrix[nx][ny]:
                if 0<=nx<M and 0<=ny<N and matrix[x][y] < matrix[nx][ny]:
                    #visited.add((nx,ny))
                    bestNeighborDepth = max(bestNeighborDepth,dfs(nx,ny)+1)
                    #visited.remove((nx,ny)) #backtrack
            memo[x][y] = bestNeighborDepth
            return bestNeighborDepth
        
        #iterate through each coord in matrix and do dfs with that coord as the start
        for i in range(M):
            for j in range(N):
                depth = dfs(i,j) + 1
                if depth > self.maxLength:
                    self.maxLength = depth
        #print(memo)
        return self.maxLength

def main():
    
    input = ""

    expected = ""

    inputs = []
    
    testingOneInput = True
    if testingOneInput:
        #Test single input
        print("Input: {}".format(input))

        solution = Solution()
        output = solution.func(input)
        print("Output: {}".format(output))
        #print("Output == Expected: {}".format(output==expected))
    """
    else:
        #Test multiple inputs
        solution = Solution()
        for input in inputs:
            output = solution.func(input)
            print("Input: {0}, Output: {1}".format(input, output))
    """
        
if __name__ == main():
    main()