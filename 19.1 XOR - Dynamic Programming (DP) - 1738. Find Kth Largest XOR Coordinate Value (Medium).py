"""
Victor Zheng
01-23-2021
1738. Find Kth Largest XOR Coordinate Value (Medium)
""" 
"""
Approach: O(m*n) runtime, O(m*n) space - 4236ms(58.29%), 63.8MB(12.78%)
Use dp to fill XOR matrix
Also fill heap to return k max easily
dp[x][y] = dp[x-1][y] ^ dp[x][y-1] ^ dp[x-1][y-1] #since bottom and right areas overlap on dp[x-1][y-1], they cancel at dp[x-1][y-1], so we have to throw back in dp[x-1][y-1]
"""
from typing import List
import heapq
#Finished but 13mins after contest ended - Weekly Contest 225)
class Solution:
    def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:
        m = len(matrix)
        n = len(matrix[0])
        dp = [[-1 for _ in range(n)] for _ in range(m)]
        dp[0][0] = matrix[0][0]
        pq = []
        heapq.heappush(pq,-1*dp[0][0])
        for x in range(m):
            for y in range(n):
                if x == 0  and y == 0:
                    continue
                if x > 0 and y > 0:
                    dp[x][y] = dp[x-1][y] ^ dp[x][y-1] ^ dp[x-1][y-1] ^ matrix[x][y]
                    #print(x,y,dp[x-1][y],dp[x][y-1],dp[x-1][y-1],dp[x][y],matrix[x][y])
                elif x == 0:
                    dp[x][y] = dp[x][y-1] ^ matrix[x][y]
                    #print(x,y,dp[x][y-1],matrix[x][y],dp[x][y])
                elif y == 0:
                    dp[x][y] = dp[x-1][y] ^ matrix[x][y]
                    #print(x,y,dp[x-1][y],matrix[x][y],dp[x][y])
                heapq.heappush(pq,-1*dp[x][y])
        #print(dp)
        retVal = -1
        while k > 0:
            retVal = -1 * heapq.heappop(pq)
            k -= 1 
        return retVal

def main():
    """
    [[5,2],[1,6]]
    1
    [[5,2],[1,6]]
    2
    [[5,2],[1,6]]
    3
    [[5,2],[1,6]]
    4
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
#Problem 3 (Weekly Contest 225)
#fail 1
class Solution:
    def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:
        #use dp to fill XOR matrix
        #also fill heap to return k max easily
        m = len(matrix)
        n = len(matrix[0])
        dp = [[-1 for _ in range(m)] for _ in range(n)]
        dp[0][0] = matrix[0][0]
        pq = []
        heapq.heappush(pq,-1*dp[0][0])
        
        for x in range(m):
            for y in range(n):
                if x == 0  and y == 0:
                    continue
                if y > 0:
                    dp[x][y] = dp[x][y-1] ^ matrix[x][y]
                elif x > 0:
                    dp[x][y] = dp[x-1][y] ^ matrix[x][y]
                heapq.heappush(pq,-1*dp[x][y])
        print(dp)
        while k>0:
            retVal = -1 * heapq.heappop(pq)
            k -= 1 
        return retVal
"""