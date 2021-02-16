"""
Victor Zheng
01-01-2021
130. Surrounded Regions (Medium)
Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'. 
Two cells are connected if they are adjacent cells connected horizontally or vertically.
""" 
"""
Approach1:
Use dfs from every "O" that is on the boarders and convert all those "O" that are connected into "A" which temporarily
means they are explored, but will turn back to "O" at the end of the dfs. After finishing dfs on all boarder "O", 
we can then iterate through the entire board and convert all "O" into "X", and "A" into "O".

Discussion post: https://leetcode.com/problems/surrounded-regions/discuss/997133/Python-3-DFS-and-backtracking-with-explanation-(128ms-runtime-O(1)-extra-space)
"""
from typing import List
class Solution:
    # 128ms ~ O((M+N) * 3^(M*N))) (upperbound) runtime. The first M+N is from looking through the boundary, and 3^(M*N) for dfs up to a maximum depth of M*N nodes 
    # M+N is dependent on 3^(M*N) if we have 3^(M*N) on the first dfs search, then the rest of the M+N-1 iterations won't be searched past the first node
    # which means it's just O(3^(M*N) + (M+N-1)), but likewise (M+N) will increase if 3^(M*N) is decreased.

    # O(1) extra space used, we only need to modify the given input board, rather than making a new one.

    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        if not board or len(board[0]) == 0:
            return
        
        rows = len(board)
        cols = len(board[0])
        
        # input a boarder "O" position, and convert all connected "O" into "A"
        def dfs(x,y):
            board[x][y] = "A"
            # check the neighbors
            for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                newX, newY = x + dx, y + dy
                
                # check for bounds
                if 0 <= newX < rows and 0 <= newY < cols:
                    if board[newX][newY] == "O":
                        dfs(newX,newY)
            return
        
        # iterate through the boundary of the board and insert any "O" into dfs
        # top boundary
        x = 0
        for y in range(cols):
            if board[x][y] == "O":
                dfs(x,y)
        # bottom boundary
        x = rows - 1
        for y in range(cols):
            if board[x][y] == "O":
                dfs(x,y)
                
        # note that left and right boundaries check top and bottom values (even though it's checked previously)
        # but that doesn't matter since the label is no longer "O" it will be "A"
        
        # left boundary
        y = 0
        for x in range(rows):
            if board[x][y] == "O":
                dfs(x,y)
        # right boundary
        y = cols - 1
        for x in range(rows):
            if board[x][y] == "O":
                dfs(x,y)
        
        # iterate through board and convert all "O" into "X" and "A" into "O"
        for x in range(rows):
            for y in range(cols):
                if board[x][y] == "O":
                    board[x][y] = "X"
                elif board[x][y] == "A":
                    board[x][y] = "O"
        
        return

def main():
    
    input = ""

    inputs = []
    
    testingOneInput = True
    if testingOneInput:
        #Test single input
        print("Input: {}".format(input))

        solution = Solution()
        output = solution.func(input)
        print("Output: {}".format(output))
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