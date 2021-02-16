"""
Victor Zheng
02-15-2021
525. Contiguous Array (Medium0)
""" 
"""
Approach1: O(N^2) runtime, O(1) space
brute force - sliding window
1) Start from left=right=0, 
2) Iterate right pointer all the way right and count the ones and zeros.
3) Keep shifitng right pointer backwards until ones=zeros or left > right. 
4) Then shift left forward one and repeat instructions 2-4
"""

"""
Approach2: O(N) runtime, O(N) space (worst case we have N different levels ex: [1,1,1,1,1,1,1]) - 784ms(99.65%), 19MB(18.18%)
Using Hashmap - dict[level] = index

Idea from - https://leetcode.com/problems/contiguous-array/solution/
"""
from typing import List 
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        
        N = len(nums)
        if N <= 1:
            return 0
        
        levelToIndex = {}
        levelToIndex[0] = -1 #start off at level=0 for index=-1, this is head value
        level = 0
        bestLength = 0
        for index,num in enumerate(nums):
            #0 decrease level, 1 increase level
            level += -1 if num==0 else 1
            #print("index={},num={},level={}".format(index,num,level))
            #check if level is already obtained before and get the length of contiguous subarray
            if level in levelToIndex:
                #we hit this level before, check for length update
                curLength = index - levelToIndex[level]
                if curLength > bestLength:
                    bestLength = curLength
            else:
                #never hit this level, save it
                levelToIndex[level] = index
        #print("levelToIndex: {}".format(levelToIndex))
        return bestLength
                

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