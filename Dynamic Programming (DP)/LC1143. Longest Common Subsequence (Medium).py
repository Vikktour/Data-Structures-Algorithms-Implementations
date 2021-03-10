"""
Victor Zheng
02-03-2021
1143. Longest Common Subsequence (Medium)
Discussion: https://leetcode.com/problems/longest-common-subsequence/discuss/1048444/python-full-dp-progression-comments-reference-video
""" 
"""
Approach1: TLE
O(3^(N1+N2)) runtime (the function calls itself up to 3 times inside itself, and recurses up till the end of the length of both words)
O(N1+N2) memory for recursive stack
Recursion 
Larry provided a good thorough explanation of DP progression
https://www.youtube.com/watch?v=HrHUZRXarWI&t=622s&ab_channel=ProgrammingLivewithLarry
"""
"""
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        N1 = len(text1)
        N2 = len(text2)
        def LCSrecur(index1,index2):

            #base case, when index reaches end
            if index1 == N1 or index2 == N2:
                return 0
            
            scoreTakeShiftBoth = 0
            if text1[index1] == text2[index2]:
                #taking this index pair, and then shift both indices forward
                scoreTakeShiftBoth = LCSrecur(index1+1,index2+1) + 1
            
            #not taking this index pair and shifting index1 forward
            scoreShift1 = LCSrecur(index1+1,index2)

            #not taking this index pair and shifting index2 forward
            scoreShift2 = LCSrecur(index1,index2+1)

            #get the max of shifting1,shifting2, and shiftingBoth
            best = max(scoreTakeShiftBoth,scoreShift1,scoreShift2)
            return best
        return LCSrecur(0,0)
"""

"""
Approach2: O(N1*N2) runtime, O(N1*N2) memory - 968ms (15.73%), 33MB (21.31%)
Top-Down: Recursion + Memoization
"""
"""
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        N1 = len(text1)
        N2 = len(text2)

        dp = [[0] * N2 for _ in range(N1)]
        seen = [[False] * N2 for _ in range(N1)]

        def LCSrecur(index1,index2):
            
            #base case, when index reaches end
            if index1 == N1 or index2 == N2:
                return 0
            
            #memoization
            if seen[index1][index2]:
                return dp[index1][index2]
            
            scoreTakeShiftBoth = 0
            if text1[index1] == text2[index2]:
                #taking this index pair, and then shift both indices forward
                scoreTakeShiftBoth = LCSrecur(index1+1,index2+1) + 1
            
            #not taking this index pair and shifting index1 forward
            scoreShift1 = LCSrecur(index1+1,index2)

            #not taking this index pair and shifting index2 forward
            scoreShift2 = LCSrecur(index1,index2+1)

            #get the max of shifting1,shifting2, and shiftingBoth
            best = max(scoreTakeShiftBoth,scoreShift1,scoreShift2)

            #update memoize table
            seen[index1][index2] = True
            dp[index1][index2] = best
            return best

        return LCSrecur(0,0)
"""

"""
Approach3: O(N1*N2) runtime, O(N1*N2) memory - 488ms (38.47%), 21.9MB (80.70%)
Bottom-Up: remove recursion, and just use Memoization array
"""
"""
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        N1 = len(text1)
        N2 = len(text2)

        #initialize dynamic programming array (note that top row and left column starts off as 0)
        dp = [[0] * (N2+1) for _ in range(N1+1)]
        
        #iterate through dp array and increment everytime we see a match
        for x in range(1,N1+1):
            for y in range(1,N2+1):
                if text1[x-1] == text2[y-1]:
                    #found match
                    dp[x][y] = dp[x-1][y-1] + 1
                dp[x][y] = max(dp[x][y], dp[x-1][y], dp[x][y-1]) #take max of current,left,right positions
        
        return dp[N1][N2] #last index of dp array is our max score
"""

"""
Approach4: O(N1*N2) runtime, O(N2) space - 456ms(44.71%), 14.4MB(88.59%)
Fine Tune: Reduce the dimension of space
Note that in the previous approach, we iterate row by row, and only need to keep info of the previous row rather than the entire matrix
"""
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        N1 = len(text1)
        N2 = len(text2)

        #initialize dynamic programming array (note that top row and left column starts off as 0)
        dpPrevRow = [0] * (N2+1)
        dpCurrentRow = [0] * (N2+1)
        
        #iterate through dp array and increment everytime we see a match
        for x in range(1,N1+1):
            
            #prepares prev and current for next row of iteration
            dpPrevRow = dpCurrentRow
            dpCurrentRow = [0] * (N2+1)

            for y in range(1,N2+1):
                if text1[x-1] == text2[y-1]:
                    #found match
                    dpCurrentRow[y] = dpPrevRow[y-1] + 1
                dpCurrentRow[y] = max(dpCurrentRow[y], dpPrevRow[y], dpCurrentRow[y-1]) #take max of current,left,right positions
            
            #print("dpCurrentRow: {}".format(dpCurrentRow))
        
        return dpCurrentRow[N2] #last index of dp array is our max score

def main():
    
    text1, text2 = "abcde", "ace" #3
    text1, text2 = "abc", "def" #0
    text1, text2 = "abce", "aceb" #3
    text1, text2 = "abcba", "abcbcba" #5

    inputs = []
    
    testingOneInput = True
    if testingOneInput:
        #Test single input
        print("Input: text1={}, text2={}".format(text1,text2))

        solution = Solution()
        output = solution.longestCommonSubsequence(text1,text2)
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