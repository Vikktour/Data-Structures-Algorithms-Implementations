"""
Victor Zheng
03-24-2021
870. Advantage Shuffle (Medium)
Discuss: https://leetcode.com/problems/advantage-shuffle/discuss/1125525/Python-Greedy-Two-Pointer-Map-or-ExplanationandComments
""" 
"""
Approach: O(NlogN) runtime (due to sort), O(N) space - where N = len(A) = len(B)
Greedy, Two-Pointer, Map

1) Sort A and B. 
We will create a copy of B since we will need to know it's original indices in order to do the mapping for A at the end.

2) Create a mapping of BtoA (each **b** value will map to a list of **a**)
Have a pointer on left&right ends of B. 
For each A[i], we want to map it to B[left] if a > b otherwise map it to B[right] (meaning this **a** will not count as an advantage). 
Note that we're greedly mapping **a** to lowest **b** if it satisifes a > b, 
and otherwise map **a** to max available **b** so that the lower **b** can be saved for mapping to other higher **a**.

Our mapping structure will be BtoA maps [b]-->[[aList],index] where aList stores multiple a's in the case where there are duplicate **b**'s. 
Index is a pointer that keeps track of which **a**'s we've used so far. Index will be 0 until we start assigning the A (done ihn the last for loop)

3) Assign the result A
For each index in A, we look at B[index] and assign A[index] according to our mapping of bList[bListIndex]-->a.
We need to make sure to increment bIndex so in the future we're not reusing the same positional b in bList.

Ex: A = [2,0,4,1,2], B = [1,3,0,0,2]
1) A = [0,1,2,2,4], Bsorted = [0,0,2,1,3]
2) BtoA = {3: [[0], 0], 0: [[1, 2], 0], 1: [[2], 0], 2: [[4], 0]}
3) Aresult = [2,0,1,2,4]
"""
from typing import List 
#Fail didn't take into account duplicates for B, which caused the map to replace previous maps instead of appending
"""
class Solution:
    def advantageCount(self, A: List[int], B: List[int]) -> List[int]:
        N = len(A) # == len(B)
        
        BtoIndex = {b: i for i,b in enumerate(B)}

        A.sort()
        Bsorted = sorted(B)
        
        aPtr = 0
        bLeft = 0
        bRight = N - 1
        BtoA = {}
        while aPtr < N:
            if A[aPtr] > Bsorted[bLeft]:
                #map B[bLeft] to a
                BtoA[Bsorted[bLeft]] = A[aPtr]
                bLeft += 1
            else:
                #map b[bRight] to a since we can't pair a with anything else, we might as well pair it with highest unused b value so the lower b values can still match with other a
                BtoA[Bsorted[bRight]] = A[aPtr]
                bRight -= 1
            aPtr += 1
        
        for index in range(N):
            A[index] = BtoA[B[index]]
        return A
"""
class Solution:
    def advantageCount(self, A: List[int], B: List[int]) -> List[int]:
        N = len(A) # == len(B)

        #1. Sort A and B
        A.sort()
        Bsorted = sorted(B)

        #2. Create a mapping of BtoA 
        aPtr = 0
        bLeft = 0
        bRight = N - 1
        BtoA = {}
        while aPtr < N:
            a = A[aPtr]
            if a > Bsorted[bLeft]:
                #map B[bLeft] to a
                b = Bsorted[bLeft]
                bLeft += 1
            else:
                #map b[bRight] to a since we can't pair a with anything else, we might as well pair it with highest unused b value so the lower b values can still match with other a
                b = Bsorted[bRight]
                bRight -= 1
                
            #mapping is done here
            if b not in BtoA:
                BtoA[b] = [[a],0]
            else:
                BtoA[b][0].append(a)
            aPtr += 1
        #print("BtoA: {}".format(BtoA))

        #3. Assign the result A
        for index in range(N):
            bList,bListIndex = BtoA[B[index]]
            A[index] = bList[bListIndex]
            BtoA[B[index]][1] += 1
        return A

"""
Approach2: 
Priority Queue
"""

def main():
    """
    [2,7,11,15]
[1,10,4,11]
[12,24,8,32]
[13,25,32,11]
[2,0,4,1,2]
[1,3,0,0,2]
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
Solution by majnu (from Larry's Discord)
SortedList - pop is O(logN)
"""
"""
from sortedcontainers import SortedList

class Solution:
    def advantageCount(self, A: List[int], B: List[int]) -> List[int]:
        nums = SortedList(A)
        
        N = len(B)
        
        res = []
        for i in range(N):
            just_larger_idx = nums.bisect_right(B[i])
            #if B[i] bisects sorted(A) at rightend (meaning we can't map this B to get points) then we use smallest a value to map to B[i]
            if just_larger_idx == len(nums):
                res.append(nums[0])
                nums.pop(0)
            #otherwise this B[i] can be mapped to A[just_larger_idx], because A[just_larger_idx] > B[i], so we append that to result
            else:
                res.append(nums[just_larger_idx])
                nums.pop(just_larger_idx)
        return res
"""