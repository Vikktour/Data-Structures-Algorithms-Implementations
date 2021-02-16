"""
Victor Zheng
12-14-2020
131. Palindrome Partitioning (Medium)
https://leetcode.com/problems/palindrome-partitioning/
""" 
"""
Approach: 
Backtracking
https://leetcode.com/problems/palindrome-partitioning/solution/
https://drive.google.com/file/d/1F4lw5PSyLY6PfAiy5y5CTwcw_Vqeqhih/view?usp=sharing
"""

from typing import List
class Solution:
    #700ms ~ O(n * 2^n) runtime (2^n-1 possible partitions, and n for ispallindrome/slicing)
    #O(n^2) memory - n for longest branch, another n for storing left/right on each node
    def partition(self, s: str) -> List[List[str]]:

        def isPalindrome(s: str) -> bool:
            return s == s[::-1] #check if s is the same as s.reverse()

        self.partitions = []
        strLen = len(s)
        #left stores the list of strings that are palindromes thusfar, and right stores the string we have yet to parse
        def dfsSplit(left:List[str],right:str,splitIndex:int):
            
            #base case: run out of right string to apend
            if right == "":
                self.partitions.append(left)
                #print("partitions: {}".format(self.partitions))
                return
            
            spltLenMax = strLen-splitIndex+1
            prevLeft, prevRight = left[:], right #this is for resetting the left,right at the start of each loop
            #print("prevLeft={},prevRight={}".format(prevLeft,prevRight))
            for splitLen in range(1,spltLenMax):
                left,right = prevLeft[:],prevRight
                #print("top of for loop left={},right={}".format(left,right))
                if len(right) < splitLen:
                    #not enough chars to take from right
                    return 
                #split rightString at splitIndex
                middle = right[0:splitLen]
                #print("splitLen={}, left={}, middle={}, right={}".format(splitLen,left,middle,right))
                if isPalindrome(middle):
                    #if middle is a palindrome then keep going
                    right = right[splitLen::]
                    #print("splitLen={}, left={}, middle={}, right={}".format(splitLen,left,middle,right))
                    left.append(middle)
                    #print("dfsSplit of: left={},right={},ssplitIndex={}".format(left[:],right,splitIndex+splitLen))
                    dfsSplit(left[:],right,splitIndex+splitLen) #note we're passing left's list as a value, not reference
                #else:
                    #not a pallindrome, so the entire set for this path is invalid
                    #return 
            
        dfsSplit([],s,0)
        return self.partitions
        



def main():
    
    input = "aab" #[["a","a","b"],["aa","b"]]
    #input = "a" #[["a"]]

    inputs = []
    
    testingOneInput = True
    if testingOneInput:
        #Test single input
        print("Input: {0}".format(input))

        solution = Solution()
        output = solution.partition(input)
        print("Output: {0}".format(output))
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