"""
Victor Zheng
04-01-2021
572. Subtree of Another Tree (Easy)
""" 
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""
Approach1: O(S*T) runtime O(S) space - where S=len(s) and T=len(t)
At each node of s, we check if it's a root for subtree of t.
I'll use iterative dfs to loop through each node of s. I'll use a function check() which comprares the node to see if it has the same structure as subtree t.
"""

class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        
        if s == None:
            if t == None:
                return True
            else:
                return False
        
        #compare node a with node b to see if they have the same structure. We will insert a from s and b from t
        def check(a,b) -> bool:
            #if not b: #this is for the case where the subtree can be anywhere in a (not necessarily the bottom) - whenever b reaches the end, we don't care about a is because b is already matched to the leaf node
            if not a and not b: #the problem wants no extra nodes under a even after matching b, so we use "and"
                return True
            elif a and b:
                if a.val != b.val:
                    return False
                #check left and right. To be a subtree, both left and right have to be the same (i.e. both must return true)
                left = check(a.left,b.left)
                right = check(a.right,b.right)
                return left and right
            else:
                #not a xor not b
                return False
        
        #dfs through s and check if at any point we find a root that contains subtree t
        stack = []
        stack.append(s)
        while stack:
            node = stack.pop()
            if check(node,t):
                return True
            #check children to see if they are root of subtree t
            #append right, then left, so we're always popping left (dfs leftfirst)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
            
        return False

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