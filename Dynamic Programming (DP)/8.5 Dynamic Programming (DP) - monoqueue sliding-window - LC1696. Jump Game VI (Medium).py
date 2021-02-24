"""
Victor Zheng
02-23-2021
1696. Jump Game VI (Medium)
I wasn't able to answer this on Leetcode Weekly Contest 220 - 12-19-2021
Discussion: https://leetcode.com/problems/jump-game-vi/discuss/1080996/Python-DP-progression-or-Monoqueue-or-explanationandcomments
""" 

"""
Approach1.1: TLE - O(N*k^N) runtime, O(N) space
DP - recursion without memoization
"""
from typing import List
class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        N = len(nums)
        def recur(index,bestSum):
            #print("bestSum: {}".format(bestSum))
            if index >= N-1:
                return bestSum
            
            prevSum = bestSum
            bestSum = float("-inf")
            for nextIndex in range(index+1,index+k+1):
                #print("nextIndex: {}".format(nextIndex))
                if nextIndex == N:
                    #print("break; index={},nextIndex={}".format(index,nextIndex))
                    break
                #print("prevSum={},nums[nextIndex]={}".format(prevSum,nums[nextIndex]))
                bestSum = max(bestSum, recur(nextIndex,prevSum+nums[nextIndex]))
            
            #print("bestSum: {}".format(bestSum))
            return bestSum
        
        return recur(0,nums[0])

"""
Approach1.2: TLE - O(k^N) runtime, O(N) space
DP - recursion with memoization 
"""
from functools import lru_cache
class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        N = len(nums)
        
        cache = {} #maps (index,curSum) to maxSum 

        #@lru_cache(maxsize=None)
        def recur(index,bestSum):
            #print("bestSum: {}".format(bestSum))
            if index >= N-1:
                return bestSum
            
            prevSum = bestSum
            bestSum = float("-inf")
            for nextIndex in range(index+1,index+k+1):
                #print("nextIndex: {}".format(nextIndex))
                if nextIndex == N:
                    #print("break; index={},nextIndex={}".format(index,nextIndex))
                    break
                #print("prevSum={},nums[nextIndex]={}".format(prevSum,nums[nextIndex]))
                
                sumUpTillNextIndex = prevSum+nums[nextIndex]
                if (nextIndex,sumUpTillNextIndex) not in cache:
                    cache[(nextIndex,sumUpTillNextIndex)] = recur(nextIndex,sumUpTillNextIndex)
                
                nextIndexBestSum = cache[(nextIndex,sumUpTillNextIndex)]
                bestSum = max(bestSum, nextIndexBestSum)
            
            #print("bestSum: {}".format(bestSum))
            return bestSum
        
        result = recur(0,nums[0])
        return result

"""
Approach1.3a- O(N*k) runtime - TLE
DP - bottom-up check previous k digits and dp[index] = nums[index] + maxOfPrevK.
Here we need to find the max value for every k window, so it will cost k iterations for every N iteration.
"""
    
"""
Approach1.3b- O(N) runtime, O(N+k) space - 1081ms(32.56%), 28MB(90%)
Similar to approach1.3a, but now keep track of monotonic decreasing stack of (value,index).
Note that we don't need to store the value as index can easily retrieve the value, but I'm did it because it was easier for me to understand when I first coded it.
"""
import collections

class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        
        N = len(nums)
        
        dp = nums[:]
        stack = collections.deque() #(value,index)
        stack.append((dp[0],0))
        
        for index in range(1,N):
            
            #remove any indices in stack that are expired (i.e. out of window [index-k,index])
            while index - k > stack[0][1] :
                stack.popleft()
            
            #check previous k values to see which one is max (i.e. our first item in stack)
            prevDpMaxIdx = stack[0][1]
            dp[index] = dp[prevDpMaxIdx] + nums[index]
            
            #add our current index to stack
            while stack and stack[-1][0] <= dp[index]:
                stack.pop()
            stack.append((dp[index],index))
            
        return dp[-1]

"""
Approach1.3c: O(N) runtime O(k) space - 980ms(57.10%), 28.3MB(57.92%)
Extra optimization of Approach1.3b
1) Saved the need to create another list for dp by modifying our input nums and use it as dp. 
2) Also instead of storing (value,index), we only store index because it can also be used to lookup prev dp value.
"""

class Solution:
    def maxResult(self, dp: List[int], k: int) -> int:
        
        N = len(dp)
        
        #dp = nums #our dp can just refer to nums (so we don't create a new list of length N)
        stack = collections.deque() #(value,index)
        stack.append(0)
        
        for index in range(1,N):
            
            #remove any indices in stack that are expired (i.e. out of window [index-k,index])
            while index - k > stack[0] :
                stack.popleft()
            
            #check previous k values to see which one is max (i.e. our first item in stack)
            prevDpMaxIdx = stack[0]
            dp[index] = dp[prevDpMaxIdx] + dp[index]
            
            #add our current index to stack
            while stack and dp[stack[-1]] <= dp[index]:
                stack.pop()
            stack.append(index)
            
        return dp[-1]

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

"""
Approach0.1:
Sliding window with max windowsize k.
Greedy - always take the next closest positive number.

Interesting cases
k=3
5,5,-10,-100,-100
-10,-100,-1000,-10000,1
-10,-1000,-100,-10000,-100

-10,-10,-15,-30,-40,1 #0,2,5 #greedy doesn't work here
"""