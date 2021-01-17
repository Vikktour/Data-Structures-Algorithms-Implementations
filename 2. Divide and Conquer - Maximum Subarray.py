"""
Victor Zheng
01-16-2020
53. Maximum Subarray (Easy)

""" 
from typing import List
"""
Approach1: O(nlogn) runtime, O(logn) memory (recursive stack) - 152ms, 15.2MB
Using divide and conquer. This is not the most efficient solution, but is a great example of implementing divide and conquer.

Good visualization videos
https://www.youtube.com/watch?v=yBCzO0FpsVc&ab_channel=GhassanShobakiComputerScienceLectures
https://www.youtube.com/watch?v=u7YMFRUFqe0&ab_channel=AlgorithmsMadeEasy
"""
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
		
		#divide and conquer recursive function
        def daq(left,right) -> int:
            if left == right:
                return nums[left]
            #divide
            middle = (left + right) // 2
            leftMax = daq(left,middle)
            rightMax = daq(middle+1,right)
            crossMax = crossmax(left,right,middle)
			#join
            return max(leftMax,rightMax,crossMax)
		
		#gets the max sum that includes both the left and right half (note that leftmax or rightmax can be bigger)
        def crossmax(left,right,middle) -> int:
            #start from middle and calculate cumulative sum leftwards to find maxleftsum and same for right.

            #find max cumulative from middle to left
            leftSum = 0
            leftSuffixMax = float("-inf")
            for pointer in range(middle,left-1,-1):
                leftSum += nums[pointer]
                leftSuffixMax = max(leftSuffixMax,leftSum)

            #find max cumulative from middle+1 to right
            rightsum = 0
            rightPrefixMax = float("-inf")
            for pointer in range(middle+1,right+1):
                rightsum += nums[pointer]
                rightPrefixMax = max(rightPrefixMax,rightsum)
            #note that rightPrefixMax may still be -inf if there's no right elements, or negative int if there are negative right elements
            #we need at least one element on the right anyways in order to consider it a crossSum (requires at least one element in both left and right)
            
            return leftSuffixMax + rightPrefixMax
                
        return daq(0,len(nums)-1)
            
        
"""
Approach2: O(n) runtime, O(1) extra memory
Dynamic programming: At each index, we keep suffixsum if it's > 0 (because it can create new), and reset to 0 otherwise.
max: suffixsum+nums[i]
"""

"""
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        suffixsum = 0
        curMax = -1*float("inf")
        for num in nums:
            curVal = suffixsum + num 
            if curVal > curMax:
                curMax = curVal
            suffixsum = max(0,suffixsum+num)
        return curMax
"""

def main():
    
    input = [-2,1,-3,4,-1,2,1,-5,4] #6
    #input = [1] #1
    #input = [-1] #-1

    inputs = []
    
    testingOneInput = True
    if testingOneInput:
        #Test single input
        print("Input: {}".format(input))

        solution = Solution()
        output = solution.maxSubArray(input)
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