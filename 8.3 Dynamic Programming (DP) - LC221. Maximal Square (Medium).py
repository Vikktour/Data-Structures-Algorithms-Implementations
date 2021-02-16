"""
Victor Zheng
02-12-2021
221. Maximal Square (Medium)
""" 
"""
Approach: O(m*n) runtime, O(1) extra space - 216ms(40.97%), 17.4MB (8.59%)
Bottom-Up Dynamic programming - dp[i][j] depends on left,top,top-left values.
A bigger square of dimension K+1 is formed when the previous 3 values are all squares of dimension K.
Note that we don't return the last value at the end, but keep track of the maximum square throughout the iteration;
this is sort of using Kadane's algorithm.
Diagram: https://drive.google.com/file/d/1f3pMJhWnc3b7zQZwCADZpaVY_2TteDVI/view?usp=sharing
Discussion: https://leetcode.com/problems/maximal-square/discuss/1062538/Python-Bottom-Up-DP-short-explanation-and-diagram
"""
from typing import List
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        #dp = [[0] * n for _ in range(m)]
        
        #dp[i][j] looks at topleft,top,left values
        #since there's no rules about modifying input matrix, we can use our input matrix as our dp matrix to be memory efficient
        
        #initialize maxSquareSide to be 0 (or 1 if there's a 1 in first row or col)
        maxSquareSide = 0 #our current max square side length
        for val in matrix[0]:
            #first row
            if val == "1":
                maxSquareSide = 1
                break
        if maxSquareSide == 0:
            for i in range(m):
                #first col
                if matrix[i][0] == "1":
                    maxSquareSide = 1
                    break
        
        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][j] == "1":
                    matrix[i][j] = str(min(int(matrix[i-1][j-1]),int(matrix[i-1][j]),int(matrix[i][j-1])) + 1)
                if int(matrix[i][j]) > maxSquareSide:
                    maxSquareSide = int(matrix[i][j])
        #print(matrix)
        return maxSquareSide**2

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