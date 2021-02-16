"""
Victor Zheng
01-11-2021
88. Merge Sorted Array (Easy)
""" 
"""
Approach: O(n) runtime, O(1) extra space
1) move values of nums1 to end of array
Ex:
nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
nums1 --> [0,0,0,1,2,3]

2) iterate between nums1[shiftidx] and nums2[i] and take the min and place in nums1 in order from left to right. Replace used values with 0.
nums1 = [1,0,0,0,2,3] nums2 = [2,5,6]
nums1 = [1,2,0,0,0,3] nums2 = [2,5,6]
nums1 = [1,2,2,0,0,3] nums2 = [0,5,6]
nums1 = [1,2,2,3,0,0] nums2 = [0,5,6]
nums1 = [1,2,2,3,5,0] nums2 = [0,0,6]
nums1 = [1,2,2,3,5,6] nums2 = [0,0,0]
Note that setting to 0 is not necessary, but is easier for visualization.

Discussion post: https://leetcode.com/problems/merge-sorted-array/discuss/1011844/python-3-pointer-indexing-with-explanation-on-runtime-o1-extra-space
"""
from typing import List
class Solution:
    #36ms ~ O(n) runtime, O(1) extra space
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        #move nums1 values to the end of nums1
        for index in range(m-1,-1,-1):
            nums1[index+n] = nums1[index]
            if n != 0:
                nums1[index] = 0
        
        #iterate nums1 & nums2, and put the min in front of nums1
        idx1 = n
        idx2 = 0
        idx1Left = 0
        while idx1 < len(nums1) and idx2 < len(nums2):
            if nums1[idx1] <= nums2[idx2]:
                min = nums1[idx1]
                nums1[idx1] = 0
                idx1 += 1
            else:
                min = nums2[idx2]
                nums2[idx2] = 0
                idx2 += 1

            nums1[idx1Left] = min
            idx1Left += 1
        
        #one of the arrays are done iterating, fill with the other orray
        if idx1 == len(nums1):
            #fill array with rest of nums2
            while idx2 < len(nums2):
                nums1[idx1Left] = nums2[idx2]
                idx2 += 1
                idx1Left += 1
        elif idx2 == len(nums2):
            #fill array with rest of nums1
            while idx1 < len(nums1):
                nums1[idx1Left] = nums1[idx1]
                idx1 += 1
                idx1Left += 1
        #print("nums1: {}".format(nums1))
        return
        
def main():
    
    nums1,m,nums2,n = [1,2,3,0,0,0], 3, [2,5,6], 3
    #nums1,m,nums2,n = [1], 1, [], 0 #[1]
    #nums1,m,nums2,n = [0], 0, [2], 1 #[2]
    nums1,m,nums2,n = [1,2,4,5,6,0],5,[3],1 #[1,2,3,4,5,6]
    
    inputs = []
    
    testingOneInput = True
    if testingOneInput:
        #Test single input
        print("Input: {},{},{},{}".format(nums1,m,nums2,n))

        solution = Solution()
        output = solution.merge(nums1,m,nums2,n)
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