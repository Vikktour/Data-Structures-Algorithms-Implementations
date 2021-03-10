"""
Victor Zheng
03-09-2021
34. Find First and Last Position of Element in Sorted Array (Medium)
""" 
"""
Approach1: O(N) runtime O(1) space
Binary search to find first occurence of target and then expand left&right for the rest of 8's
Or, since it's already linear time algo worst case, we can also do linear search for first occurrence of target.
"""

"""
Approach2: O(logN) runtime O(1) space - 80ms(90.25%)
Binary search to find leftmost point that fits target; keep shrinking interval until leftpointer crosses rightpointer.
Binary search to find rightmost point that fits target
"""
from typing import List
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        N = len(nums)
        if N == 0:
            return [-1,-1]
        #find leftmost point that has target
        left = 0
        right = N-1
        while left < right:
            mid = left + (right-left)//2
            if nums[mid] < target:
                #too small, move left forward
                left = mid + 1 #note the +1 so we toss position out no matter what
            elif nums[mid] > target:
                #too big, move right backwards 
                right = mid - 1
            else: #nums[mid] == target
                #check if mid-1 is also target and adjust +-1 accordingly
                if mid-1>=0 and nums[mid-1] == target:
                    right = mid - 1 #note this can cause left to pass right by 1, so adjust it back to left==right
                    if left > right:
                        left = right
                else:
                    right = mid
                    if left < right:
                        left += 1
        leftmost = left if nums[left]==target else -1
        
        #find rightmost point that has target
        left = 0
        right = N-1
        while left < right:            
            mid = left + (right-left)//2
            #print("left={},right={},mid={}".format(left,right,mid))
            if nums[mid] < target: #note the == is included to get rightmost
                #too small, move left forward
                left = mid + 1
            elif nums[mid] > target:
                #too big, move right backwards
                right = mid - 1 #note the -1 so we toss position out no matter what
            else: #nums[mid] == target:
                #if equal check if next position is target and adjust +- 1 accordingly
                if nums[mid+1] == target:
                    left = mid + 1
                else: #next position is not target, move right back
                    left = mid
                    if left < right:
                        right -= 1
            
        #left==right, now check if it's target
        rightmost = left if nums[left]==target else -1
        
        return [leftmost,rightmost]
        
        

def main():
    """
    [5,7,7,8,8,10]
8
[5,7,7,8,8,10]
6
[]
0
[1]
1
[1,1,2]
1
    """
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