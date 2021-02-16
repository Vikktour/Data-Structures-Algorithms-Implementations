"""
Victor Zheng
12-30-2020
79. Word Search (Medium)
""" 

from typing import List
import numpy as np
"""
Approach: dfs search
"""
"""
#TLE because I'm making a copy of tempUsed which is an extra multiplication of O(MN) runtime
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        rows = len(board)
        cols = len(board[0])
        self.usedNodes = set() #keeps track of what nodes we used already for this particular dfs search starting at i,j
        #takes in the current position and node
        def dfs(x,y,index:int) -> bool:

            #base case: we matched all of the chars in the word
            if index == len(word):
                return True

            #if not in bounds or if node is used already then return false
            if (x < 0 or x >= rows or y < 0 or y >= cols) or ((x,y) in self.usedNodes):
                return False
            
            #check for match
            if board[x][y] == word[index]:
                #found match for current index recursively check the other indices using adjacent nodes
                self.usedNodes.add((x,y))
                index += 1
                #print("index: {} = {}".format(index,board[x][y]))
                tempUsed = self.usedNodes.copy()
                left = dfs(x,y-1,index) 
                self.usedNodes = tempUsed.copy() #have to pass in a copy so we can reset to what it was during this current (x,y)
                right = dfs(x,y+1,index) 
                self.usedNodes = tempUsed.copy()
                up = dfs(x-1,y,index)
                self.usedNodes = tempUsed.copy()
                down = dfs(x+1,y,index)
                return left or right or up or down 
        
        for i in range(rows):
            for j in range(cols):
                #print("checking ({},{})".format(i,j))
                self.usedNodes = set() 
                existInIJ = dfs(i,j,0)
                if existInIJ:
                    return True
        return False 
"""

"""
Approach2: Instead of making a copy of the set each time, we can modify the set and at the of each dfs back track, we undo the set.add()
"""
"""
Approach3: Instead of using sets, we can modify the original input board to become " " (a nonused character) and at the end of each dfs call, we revert the character back.
So we no longer need to create extra M*N matrix which saves both runtime and memory by a factor of O(MN)
https://www.youtube.com/watch?v=vYYNp0Jrdv0&ab_channel=KevinNaughtonJr.
Another thing I added was to early break out in for loop so we don't have to search the other paths when we found one path working already.
Idea from: https://leetcode.com/problems/word-search/discuss/986610/Python-DFS-with-backtracking
"""
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # 364ms ~ O(MN*3^(M*N)) worse case runtime. MN for the double for loop, 
        # and 3^(M*N) for each starting point we can expand up to 3 (excluding the first one that can be up to 4) new tiles, and DFS goes for up to M+N nodes.
        # note that MN directly depends on 3^(M*N) (lower MN means higher 3^(M*N), and higher MN means lower 3^(M*N))

        # UPDATE FOR TIME COMPLEXITY: note that it's also capped by word length, i.e. O(MN*3^(wordLength) since we no longer search beyond the last letter of the word.
        # Note that leetcode doesn't use absolutely worse case scenarios like
        # board = [["A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A"],["A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A"],["A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A"],["A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A"],["A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A"],["A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A"],["A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A"],["A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A"],["A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A"],["A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A"],["A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A"],["A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A"],["A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A"],["A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A"],["A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A"],["A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A"],["A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A"],["A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A"],["A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A"],["A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A","A"]]
        # word = "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAB"

        # O(len(word)) extra space for dfs recursive stack
        rows = len(board)
        cols = len(board[0])
        #takes in the current position and node
        def dfs(x,y,index:int) -> bool:

            #base case: we matched all of the chars in the word
            if index == len(word):
                return True

            #if not in bounds or if node is used already then return false
            if (x < 0 or x >= rows or y < 0 or y >= cols) or (board[x][y] == " "):
                return False
            
            #check for match
            if board[x][y] == word[index]:
                #found a match for index, modify the board so we don't reuse this char in this dfs path
                tempUsedLetter = board[x][y]
                board[x][y] = " "

                index += 1
                #print("index: {} = {}".format(index,board[x][y]))
                
                for delta in [(0,-1),(0,1),(-1,0),(1,0)]:
                    dx = delta[0]
                    dy = delta[1]
                    pathWorks = dfs(x+dx,y+dy,index)
                    if pathWorks:
                        #we found a path so don't need to search the rest
                        break

                #revert back the board
                board[x][y] = tempUsedLetter
                return pathWorks
        
        for i in range(rows):
            for j in range(cols):
                #print("checking ({},{})".format(i,j))
                existInIJ = dfs(i,j,0)
                if existInIJ:
                    return True
        return False 

def main():
    board,word = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED" #True
    #board,word = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "SEE" #True
    board,word = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCB" #False
    #board,word = [["a"]], "a" #True
    #board,word = [["a","a","a"]], "aaa" #True
    board,word = [["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]], "ABCESEEEFS" #True


    inputs = []
    
    testingOneInput = True
    if testingOneInput:
        #Test single input
        npBoard = np.array([np.array(xi) for xi in board])
        print("Input: \n board= \n {0} \n word={1}".format(npBoard,word))

        solution = Solution()
        output = solution.exist(board,word)
        print("Output: {0}".format(output))
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