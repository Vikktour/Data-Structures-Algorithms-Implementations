"""
Victor Zheng
01-23-2021
1727. Largest Submatrix With Rearrangements (Medium)
""" 
"""
Approach: O(m*nlogn) runtime O(1) space - 1116ms (97.79%), 40.7MB (47.17%)
Compute suffixsum from top to bottom. Reset everytime we reach a 0.
Now go to each row and compute area for each value (starting from right to left). For each value, we will use all values to the right of it (including itself) to compute area.
So basically we are getting the area for each given value in the row.
Diagram example: https://drive.google.com/file/d/1W0LWFdMwXqstlwySBERkJ_I11QWIq-0V/view?usp=sharing
Note that the sorting of the previous row would not ruin the answer obtained from calculating area in the next row because we're using suffix sum.

Discussion post: https://leetcode.com/problems/largest-submatrix-with-rearrangements/discuss/1031282/python-suffix-sum-sort-rows-compute-areas-omnlogn-runtime-with-explanation
"""
from typing import List
import numpy as np #for printing
class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        
        m = len(matrix)
        n = len(matrix[0])

        #get suffix sum of rows (reset upon hitting 0)
        for j in range(n):
            for i in range(m):
                #for each column iterate down the rows and calculate suffix sum
                if i > 0:
                    if matrix[i][j] != 0:
                        #0 means reset
                        matrix[i][j] += matrix[i-1][j]
        
        #print(np.array(matrix))

        #iterate through each row, sort, and compute max area
        maxArea = 0
        for row in matrix:
            row.sort()
            #iterate from right to left and compute area for each set of number
            index = len(row) - 1
            while index >= 0:
                #get value
                value = row[index]
                #keep going left if it's still the same value
                while index-1 >= 0 and row[index-1] == value:
                    index -= 1
                #compute area (we multiply value by the number of items to the right including itself)
                area = value * (len(row)-index)
                if area > maxArea:
                    maxArea = area
                index -= 1
        return maxArea



def main():
    
    input = [[0,0,1],[1,1,1],[1,0,1]] #4
    input = [[1,0,1,0,1]] #3
    input = [[1,1,0],[1,0,1]] #2
    input = [[0,0],[0,0]] #0
    input = [[1]] #1

    inputs = []
    
    testingOneInput = True
    if testingOneInput:
        #Test single input
        print("Input: \n{}".format(np.array(input)))

        solution = Solution()
        output = solution.largestSubmatrix(input)
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