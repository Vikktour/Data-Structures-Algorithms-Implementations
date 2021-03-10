"""
Victor Zheng
02-08-2021
658. Find K Closest Elements (Medium)
""" 
"""
Approach1: O(logN + k) runtime, O(K) space (for return) - 288ms (77.39%), 15.6MB (79,19%)
1) Use binary search to find the index of the value cloest to x in the pre-sorted arr.
2) Then take the k closest values to the index obtained from (1) by using sliding window (expand left or right based on which one is closer to x, and lower in value).
"""
from typing import List
"""
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        N = len(arr)
        left = 0
        right = N-1
        mid = (left + right)//2
        
        #binary search to find index closest to x
        while left < right:
            curVal = arr[mid]
            if curVal == x:
                 break
            elif curVal > x:
                right = mid - 1
            else: #curval < x
                left = mid + 1   
            mid = (left + right)//2
        #print("potential mid: {}".format(mid))
        #mid may be off by 1, so check mid-1,mid,mid+1 to see which one is closest to x
        for shift in [1,0,-1]: #note i go in decreasing order because i want to see if the leftmost one matches (we want the lowest value first)
            potentialMid = mid + shift
            if 0 <= potentialMid < N:
                if abs(arr[potentialMid] - x) <= abs(arr[mid] - x):
                    #this mid is better
                    mid = potentialMid
        #print("best mid: {}".format(mid))
        
        #have left and right pointers start out at mid, and expand them outwards until we reach a window of length k ~O(k)
        left = right = mid
        while right-left+1 < k:
            if left-1 >= 0 and right+1 < N:
                #take the one that is closer to x
                #print("absLeft,absRight: {},{}".format(abs(arr[left-1] - x),abs(arr[right+1] - x)))
                if abs(arr[left-1] - x) <= abs(arr[right+1] - x):
                    #left is closer, so take left #Note that there's "=" to follow the description, where we take smaller one first
                    left -= 1
                else:
                    right += 1
            elif right == N - 1:
                #no more on the right, keep taking left
                left -= 1
            else: #left == 0
                #no more left, keep taking right
                right += 1
        
        #print("left,right: {},{}".format(left,right))            
        return arr[left:right+1]
"""
"""
Approach2: O(log(N-k) + k) runtime (N-k since we're binary searching on interval [0,N-k], and +k for returning list slice), O(k) space. 288ms(77.39%), 15.7MB(51.55%)
Shorter solution by shifting window with binary search
Approach from Lee: https://leetcode.com/problems/find-k-closest-elements/discuss/106426/JavaC%2B%2BPython-Binary-Search-O(log(N-K)-%2B-K)
"""
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        N = len(arr)
        left = 0
        right = N - k #right end is N-k to ensure spacing for arr[mid:mid+k]

        while left < right:
            mid = (left + right) // 2
            if x - arr[mid] > arr[mid+k] - x:
                #arr[mid] is too big, so shift left forward
                left = mid + 1
            #elif x - arr[mid] < arr[mid+k] - x:
            else:
                #arr[mid] is too small, so shift right backwards
                right = mid #note we don't do mid+1 because it might overshoot the index past N-1
            #else: #equal
            #    break
        #return arr[mid:mid+k] #off by 1
        return arr[left:left+k]

def main():
    """
    [1,2,3,3,5]
    4
    4
    [1,2,3,4,5]
    4
    3
    [1,2,3,4,5]
    4
    -1
    [0,0,1,2,3,3,4,7,7,8]
    3
    5
    [1,10,15,25,35,45,50,59]
    1
    30
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

"""
O
"""
"""
#https://leetcode.com/problems/find-k-closest-elements/discuss/133604/Clean-O(logN)-solution-in-Python
#short binary search solution that involves using binary search and shifting window
class Solution(object):
    def findClosestElements(self, arr, k, x):
        
        #:type arr: List[int]
        #:type k: int
        #:type x: int
        #:rtype: List[int]
        
        lo, hi = 0, len(arr)-k
        while lo<hi:
            mid = (lo + hi)//2
            if x-arr[mid]>arr[mid+k]-x:
                lo = mid + 1
            else:
                hi = mid
        return arr[lo:lo+k]
"""
#Lee made that solution before the above https://leetcode.com/problems/find-k-closest-elements/discuss/106426/JavaC%2B%2BPython-Binary-Search-O(log(N-K)-%2B-K)