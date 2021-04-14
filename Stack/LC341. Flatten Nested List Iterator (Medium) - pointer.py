"""
Victor Zheng
04-13-2021
341. Flatten Nested List Iterator (Medium)
""" 
"""
Approach: 
"""
class Solution:
    def func(self, s: str) -> int:
        
        return 0

def main():
    """
    [[1,2],3]
[[1,1],2,[1,1]]
[1,[4,[6]]]
[[]]
[[1]]
[[],[3]]
[[[[]]],[]]
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

    