"""
Victor Zheng
12-31-2020
84. Largest Rectangle in Histogram (Hard)
""" 
"""
Approach1: O(n^2) brute force by using two for loops and calculating the max area between any two rectangles
"""

"""
Approach2: O(n) runtime, use a stack to keep track of rectangles being added (height,index), as long as they're increasing.
Upon seeing a decrease from rect P to rect Q, we need to calculate the area of all rects that are greater than Q.
To calculate the area, we will keep track of indices and use the difference.
Note that each rect being calculated is using it's height and span the width of all rects to the right of it (up until Q).
After calculating the area of rect, pop that rect off.

After some debugging, I realized that I shouldn't be using area = poppedHeight * (index - poppedIndex) because it doesn't include
this sample case:
[1, 2, 1] which would be calculating only the last 2 indices for area, which is wrong.
The updated way tod o it is area = poppedHeight * (index - stack[-1][1] - 1) 
because we want to range it from right end to left-end where left-end contains a rect that is smaller than current rectangle we're trying to 
calculate the area for. So that means the next rectangle (i.e. to the right of the left-end) is the rectangle we want to include.
Look at the ABCDEFG example from google docs.
https://drive.google.com/file/d/1M1kx_Jky655PH7STgOqXLBAMECil3dTp/view?usp=sharing
"""
from typing import List
class Solution:
    #100ms ~ O(n) runtime, O(n) memory (worse case is when all rects are increasing)
    def largestRectangleArea(self, heights: List[int]) -> int:
        if not heights:
            return 0
        stack = [] #stores (height,index)
        stack.append((-1,-1)) #this is just a dummy value to help append the next rectangle
        maxArea = 0
        for index, height in enumerate(heights):
            if height < stack[-1][0]:
                #found a decreasing rectangle, we need to keep popping from top of stack and calculating area as long as stack[-1] > height
                while stack[-1][0] > height:
                    poppedHeight,poppedIndex = stack.pop()
                    area = poppedHeight * (index - stack[-1][1] - 1)
                    #print("area = {}*({}-{}-1) = {}".format(poppedHeight,index,stack[-1][1],area))
                    if area > maxArea:
                        maxArea = area 
            stack.append((height,index))
                    
        #at the end of the iterations, we may still have some more items on the stack if the last rectangle from above is taller than those in the stack
        #if so, calculate the area for all
        index += 1 #note that this is simulating that we take the last rectangle and use it as part of the width
        while stack[-1] and stack[-1][0] != -1:
            poppedHeight,poppedIndex = stack.pop()
            area = poppedHeight * (index - stack[-1][1] - 1)
            #print("area = {}*({}-{}-1) = {}".format(poppedHeight,index,stack[-1][1],area))
            if area > maxArea:
                maxArea = area 
        return maxArea

def main():
    
    input = [2,1,5,6,2,3] #10
    #input = [1] #1
    #input = [2,1,2] #3
    #input = [1,2,3,1.5,2.5,2,1]

    inputs = []
    
    testingOneInput = True
    if testingOneInput:
        #Test single input
        print("Input: {0}".format(input))

        solution = Solution()
        output = solution.largestRectangleArea(input)
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