"""
Victor Zheng
01-15-2021
739. Daily Temperatures (Medium)
""" 
"""
Approach1: O(n) runtime, O(n) memory (memory is based on number of temps that we haven't found a warmer temp yet) - 492ms, 18.8MB
Use sliding window to store monotone decreasing stack.
If we see an increase, then update the indicies for everything in the current window and pop it.
"""

from typing import List
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        stack = [] #store indices

        for index,temp in enumerate(T):
            #keep updating & popping the temp in stack that are less tahn current temp
            while stack and T[stack[-1]] < temp:
                stackIndex = stack.pop()
                T[stackIndex] = index - stackIndex
            #append current temp
            stack.append(index)
        
        #the rest of stack has no known warmer future dates
        while stack:
            index = stack.pop()
            T[index] = 0
        
        return T


def main():
    
    input = [73, 74, 75, 71, 69, 72, 76, 73] #[1, 1, 4, 2, 1, 1, 0, 0]

    inputs = []
    
    testingOneInput = True
    if testingOneInput:
        #Test single input
        print("Input: {}".format(input))

        solution = Solution()
        output = solution.dailyTemperatures(input)
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