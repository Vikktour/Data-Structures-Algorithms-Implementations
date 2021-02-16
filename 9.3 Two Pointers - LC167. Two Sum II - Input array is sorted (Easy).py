"""
Victor Zheng
02-07-2021
167. Two Sum II - Input array is sorted (Easy)
""" 
"""
Approach: O(N) runtime, O(1) space - 64ms (67.81%), 14.6MB (62.76%)
Two pointer - move left forward if sum is too small, move right back if too big.
Note that doing it this way instead of having right start at 0 restricts right from having to move forward and then back.
Right will always be moving backwards, keeping O(N) runtime instead of O(N^2).
"""
from typing import List
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        N = len(numbers)
        left, right = 0, N-1
        
        while left < right:
            if numbers[left] + numbers[right] < target:
                #sum is too small, move left forward
                left += 1
            elif numbers[left] + numbers[right] > target:
                #sum is too big, move right back
                right -= 1
            else:
                #sum is equal, return indices (1-indexed)
                return [left+1,right+1]
            

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