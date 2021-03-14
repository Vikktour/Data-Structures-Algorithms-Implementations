"""
Victor Zheng
03-13-2021
823. Binary Trees With Factors (Medium)
Discussions: https://leetcode.com/problems/binary-trees-with-factors/discuss/1108180/Python-Recursion-%2B-Memo-or-ExplanationandComments
""" 
"""
Approach: O(N^2) runtime O(N) space - where N=len(arr)
Recursion + Memoization
The array needs to be sorted in increasing order for this method to work.
Iterate through the array, for each array[i], we try modding with numbers to the left one by one
to find the factors of array[i]. For each factor, we can use valToCount map to lookup number of binary
trees so we don't recompute the recursion (note that there will be recursion if the factor can be broken up into more factors, so those will also be added to factors).

Diagram example: https://drive.google.com/file/d/1vwcfst55yrYAheA8glYI-enJSCd4S3x5/view?usp=sharing
"""
from typing import List 
class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        arr.sort()
        #print("sorted input={}".format(arr))
        valToCount = {} #maps arr value to number of binary trees we can make having that value as root
        MOD = 10**9+7
        result = 0
        #for each arr[i] we will get the count of all possible binary trees that have arr[i] as root, and then add it to valToCount map
        for index,val in enumerate(arr):
            valResult = 1 #start off with just [arr[i]], then add more for each binary tree we can make with factors
            #find all factors (by checking to the left of val) and multiply the count of each pair of factors to get the combination for this factor pair's orientation
            for factorIdx in range(index-1,-1,-1):
                factorCandidate = arr[factorIdx]
                if val % factorCandidate == 0:
                    #this is a factor, so get the sum of the combinations for the [thisfactor,completementfactor] orientation 
                    #(i.e. thisfactor will go first, and later on when we iterate to other arr[i], we will use the other factor to go first).
                    factor2 = val // factorCandidate
                    
                    #print("factorCandidate={},factor2={}".format(factorCandidate,factor2))
                    #check if factor2 exists in arr
                    if factor2 in valToCount:
                        #note that we can do lookups because any value to the left is already computed in the previous iteration of our first for loop
                        valResult += valToCount[factorCandidate] * valToCount[factor2]
                        valResult %= MOD
            
            #append val to map so we can reuse without having to do the whole recursion again
            valToCount[val] = valResult
            result += valResult
            result %= MOD
        
        return result

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