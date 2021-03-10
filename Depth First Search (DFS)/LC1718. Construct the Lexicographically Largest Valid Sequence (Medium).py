"""
Victor Zheng
01-19-2021
1718. Construct the Lexicographically Largest Valid Sequence (Medium)

Approach: Use dfs. Always try to put higher numbers in the front, and if we reach a deadend, then backtrack and use a lower number.
Visualization: https://www.youtube.com/watch?v=3kRBmhoA9b8&t=709s&ab_channel=HappyCoding
My diagram examples: https://drive.google.com/file/d/1TetqmIOG0SnkRtbNq1r1mAFBCExXqHee/view?usp=sharing

Complexity Analysis:

Runtime: O(n*n!)
We start by trying n at the start of the list, which means the next item on the list will be the next highest item, and going downwards as we go right.
So we have 1*(n-1)*(n-1)*...*2*1 for the first arrangement where first slot is n.
If n as start doesn't work then we need to use n-1 as start, which is another 1*(n-1)*(n-1)*...*2*1.
Now if we expect worse case, then it means we need to test out n different arrangments of having a certain value at the start.
So in total it's n*(n-1)*(n-1)*...*2*1 = n!
Also note that at each node, I'm using a for loop to check if a value is used, so the total time complexity multplied by another factor of n.
In total we have O(n*n!)

Space: O(n) 
Since we're using dfs, our max depth is 2n-1. We also store a set of up to n usedVals.

- 44ms(73,97%), 14.4MB (40.37%)
"""
from typing import List
class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        
        
        result = [-1] * (2 * n - 1) #array size is 2n-1. Fill array with -1 as indicator of not set yet.
        resultLen = len(result)
        usedVals = set()


        def dfs(index):
            #print("i={}, result: {}, usedVals: {}".format(index,result,usedVals))
            #try out all numbers for current node (dfs will recursively use the highest number first) 
            for val in range(n,0,-1):
                if val in usedVals:
                    continue
                
                if val == 1:
                    #1 is always valid, insert it and then dfs deeper
                    result[index] = val 
                    usedVals.add(val)
                    #check if we're done
                    if len(usedVals) == n:
                        return True

                    #find next available index
                    addedIndex = index
                    nextIndex = index + 1
                    while result[nextIndex] != -1:
                        nextIndex += 1
                    done = dfs(nextIndex) #done is a flag for if we found our result
                    if done:
                        return True
                    #backtrack - revert the result and usedVals 
                    result[addedIndex] = -1
                    usedVals.remove(val) 

                else:
                    #test to see if value is valid for insert
                    if (index + val < resultLen) and result[index+val] == -1:
                        #able to insert to both slots
                        result[index] = val 
                        result[index+val] = val 
                        usedVals.add(val)
                        if len(usedVals) == n:
                            return True

                        #find next available index
                        addedIndex = index
                        nextIndex = index + 1
                        while result[nextIndex] != -1:
                            nextIndex += 1
                        done = dfs(nextIndex) #done is a flag for if we found our result
                        if done:
                            return True
                        #backtrack - revert the result and usedVals 
                        result[addedIndex] = -1
                        result[addedIndex+val] = -1
                        usedVals.remove(val) 
                    else:
                        #not possible to insert, try using a lower value for this index 
                        continue
        
        dfs(0)
        return result

def main():

    #problem 3
    n = 1 #[1]
    n = 2 #[2,1,2]
    n = 3 #[3,1,2,3,2]
    n = 4 #[4,2,3,2,4,3,1]
    n = 5 #[5,3,1,4,3,5,2,4,2]
    n = 20 #[20, 18, 19, 15, 13, 17, 10, 16, 7, 5, 3, 14, 12, 3, 5, 7, 10, 13, 15, 18, 20, 19, 17, 16, 12, 14, 11, 9, 4, 6, 8, 2, 4, 2, 1, 6, 9, 11, 8]

    inputs = []
    
    testingOneInput = True
    if testingOneInput:
        #Test single input
        print("Input: {}".format(n))


        solution = Solution()
        output = solution.constructDistancedSequence(n)
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
