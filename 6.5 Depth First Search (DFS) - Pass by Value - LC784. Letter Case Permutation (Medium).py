"""
Victor Zheng
02-16-2021
784. Letter Case Permutation (Medium)
""" 
"""
Approach1: O(N*2^N) runtime, O(N*2^N) space - 56ms(74.08%), 15.6MB (8.71%)
brute force - recursively branch out each time there's a letter. I use dfs to expand string fully and append before going back to next string.
Discussions post: https://leetcode.com/problems/letter-case-permutation/discuss/1068621/Python-3-Ways-or-Optimization-or-T~O(2N)S~O(N)
"""
from typing import List
"""
class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        self.N = len(S)
        self.S = S
        self.retList = []
        curString = ""
        
        def dfs(index,curString):
            if index == self.N:
                self.retList.append(curString)
                return
            char = self.S[index]
            if char.isalpha():
                #two ways to create string - capital this letter or lowercase this letter
                dfs(index+1,curString[:]+char.upper()) #pass string in by value (copy)
                dfs(index+1,curString[:]+char.lower())
            else:
                #digit, just add it as what it is
                dfs(index+1,curString[:]+char)
                
        dfs(0,curString)
        return self.retList
"""

"""
Approach2: O(N*2^N) runtime, O(N) space - 52ms(88.03%), 15.4(26.80%)
Same as approach1 but backtrack and delete char from string - this will save space but slightly increase our runtime (constant factor)
"""
"""
class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        self.N = len(S)
        self.S = S
        self.retList = []
        self.curString = ""
        
        def dfs(index):
            if index == self.N:
                self.retList.append(self.curString)
                return
            char = self.S[index]
            if char.isalpha():
                #two ways to create string - capital this letter or lowercase this letter
                self.curString += char.upper()
                dfs(index+1)
                self.curString = self.curString[:-1] #backtrack and remove last char
                
                self.curString += char.lower()
                dfs(index+1)
                self.curString = self.curString[:-1] #backtrack and remove last char
            else:
                #digit, just add it as what it is
                self.curString += char
                dfs(index+1)
                self.curString = self.curString[:-1] #backtrack and remove last char
                
        dfs(0)
        return self.retList
"""

"""
Approach3: O(2^N) runtime, O(N) space - 60ms(58.10%), 15.4MB(33.95%)
Optimize approach2 even further; use list to represent string so we can modify at each index so there's no string slicing (because slicing creates an extra factor of N).
"""

class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        self.N = len(S)
        self.S = S
        self.retList = []
        self.curStringAsList = ["-" for _ in range(self.N)] #dummy string list, we're going to change values at each index - Note that I'm using list because string can't be modified at index
        
        def dfs(index):
            #print("curStringAsList: {}".format(self.curStringAsList))
            if index == self.N:
                self.retList.append("".join(self.curStringAsList))
                return
            char = self.S[index]
            if char.isalpha():
                #two ways to create string - capital this letter or lowercase this letter
                self.curStringAsList[index] = char.upper()
                dfs(index+1)
                self.curStringAsList[index] = char.lower()
                dfs(index+1)
            else:
                #digit, just add it as what it is
                self.curStringAsList[index] = char
                dfs(index+1)
            return
                
        dfs(0)
        return self.retList


"""
Pretty cool solution by blehart:
https://leetcode.com/problems/letter-case-permutation/discuss/115509/Python-simple-solution-(7-lines)
Start with retList and expand it on each iteration of new char.
"""
"""
class Solution:
    def letterCasePermutation(self, S):
            res = ['']
            for ch in S:
                print("ch: {}, res: {}".format(ch,res))
                if ch.isalpha():
                    res = [i+j for i in res for j in [ch.upper(), ch.lower()]]
                else:
                    res = [i+ch for i in res]
            print("res: {}".format(res))
            return res
"""

def main():
    
    """
    "a1b2"
    "3z4"
    "12345"
    "0"
    "a"
    "J2ja973hLO"
    """
    input = "1a2b3c"

    expected = ""

    inputs = []
    
    testingOneInput = True
    if testingOneInput:
        #Test single input
        print("Input: {}".format(input))

        solution = Solution()
        output = solution.letterCasePermutation(input)
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
Pretty cool solution by blehart:
https://leetcode.com/problems/letter-case-permutation/discuss/115509/Python-simple-solution-(7-lines)
Start with retList and expand it on each iteration of new char.
"""
"""
class Solution:
    def letterCasePermutation(self, S):
            res = ['']
            for ch in S:
                if ch.isalpha():
                    res = [i+j for i in res for j in [ch.upper(), ch.lower()]]
                else:
                    res = [i+ch for i in res]
            return res
"""