"""
Victor Zheng
03-22-2021
60. Permutation Sequence (Hard)
Discuss: https://leetcode.com/problems/permutation-sequence/discuss/1122554/Python-Backtrack(TLE)-IntervalSearching(O(n2))-explanation-and-comments
""" 
"""
Approach1: TLE O(n!*n*logn) runtime O(n) space - There shouldn't be a TLE based on constraints (n<=9), but LC forcefully made it so that dfs solution won't work (progbably lowered the upper time limit).
Dfs and Backtrack. Can be optimized further by using list slicing (for pop) instead of set() and sort.
"""
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        
        remaining = {i for i in range(1,n+1)}
        
        #current is a list that stores the numbers we have so far, and when it reaches size==n (remaining is empty), it is a sequence.
        #index represents the index of the sequence. I enclose it using a list in order to pass by reference in python
        def dfs(current,index):
            #print("current={},index={},remaining={}".format(current,index,remaining))
            #print("index={}, current={}".format(index,current))
            if not remaining:
                #print("index={}, current={}".format(index,current))
                index[0] += 1
                if index[0] == k:
                    return "".join([str(val) for val in current])
            
            
            remainingPrev = list(remaining)
            for num in sorted(remainingPrev): #note that set() is not sorted, so we explicitly do so
                remaining.remove(num)
                current.append(num)
                
                result = dfs(current,index)
                if result:
                    return result
                #backtrack
                poppedNum = current.pop()
                remaining.add(poppedNum)
        
        return dfs([],[0])

"""
Approach2: O(n^2) runtime O(n) space - 32ms (70%), 14.3MB
Using math - https://leetcode.com/problems/permutation-sequence/discuss/22507/%22Explain-like-I'm-five%22-Java-Solution-in-O(n)
We know that n has n! permutations.
If we choose 1 to be the first digit, then 1... has (n-1)! permutations for index = 1      to (n-1)!
If we choose 2 to be the first digit, then 2... has (n-1)! permutations for index = (n-1)!+1 to 2*(n-1)!
If we choose i to be the first digit, then i... has (n-1)! permutations for index = (i-1)*(n-1)!+1 to i*(n-1)!

So we're essentially finding which category k belongs in, and then append that digit to our result.

Let's say 2 is our first digit, then we have the option to choose a number in [1,3:n] as our second digit.
If we choose 1 to be the second digit, then 21... has (n-2)! permutations for index = (n-1)! + 1            to (n-1)! + (n-2)!
If we choose 3 to be the second digit, then 23... has (n-2)! permutations for index = (n-1)! + (n-2)! + 1   to (n-1)! + 2*(n-2)!
If we choose i to be the second digit, then 2i... has (n-2)! permutations for index = (n-1)! + i*(n-2)! + 1 to (n-1)! + i*(n-2)!
We keep moving forward and appending until we reach the last digit.

Ex: n=3,k=3
position=1
If we choose 1 to be the first digit, then 1... has (n-1)!=2 permutations for index = 1 to 2
If we choose 2 to be the first digit, then 2... has (n-1)!=2 permutations for index = 2 to 4
If we choose 3 to be the first digit, then i... has (n-1)!=2 permutations for index = 4 to 6
since k fits in for the second option, we'll use 2 as our first digit

position=2
If we choose 1 to be the second digit, then 21... has (n-2)!=1 permutations for index = 3 to 3
If we choose 3 to be the second digit, then 23... has (n-2)!=1 permutations for index = 4 to 4
Since k fits in for first option, we'll use 1 as our second digit

position=3
we only have 1 remaining option (3), so choose it
"""
import math
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        remaining = [i for i in range(1,n+1)]
        result = []
        leftbound = 1
        #iterate through position number
        for position in range(1,n+1):
            #print("position={},result={},leftbound={},remaining={}".format(position,result,leftbound,remaining))
            if len(remaining) == 1:
                #1 item left in remaining, only one way to permute
                result.append(str(remaining[0]))
                return "".join(result)
            
            #find the correct digit for this position
            for index in range(len(remaining)):
                rightbound = leftbound + (index+1)*math.factorial(n-position) - 1
                #print("index={},value={},leftbound={},rightbound={}".format(index,remaining[index],leftbound,rightbound))
                if leftbound <= k <= rightbound:
                    #k is within this interval, so accept this digit
                    digit = remaining[index]
                    result.append(str(digit))
                    leftbound = leftbound + index * math.factorial(n-position)
                    break
            remaining.pop(index)
        return "".join(result)
            


def main():
    
    n,k = 3,1
    n,k = 9,24 #"123459876"

    expected = ""

    inputs = []
    
    testingOneInput = True
    if testingOneInput:
        #Test single input
        print("Input: n={},k={}".format(n,k))

        solution = Solution()
        output = solution.getPermutation(n,k)
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