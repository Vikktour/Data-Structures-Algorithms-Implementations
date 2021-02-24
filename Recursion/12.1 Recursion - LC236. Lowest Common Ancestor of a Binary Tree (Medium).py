"""
Victor Zheng
12-13-2020
236. Lowest Common Ancestor of a Binary Tree (Medium)
""" 
"""
Approach:
https://www.youtube.com/watch?v=13m9ZCB8gjw&ab_channel=TusharRoy-CodingMadeSimple
1) Scan all the way to the leaf nodes (DFS from left to right), and check if leaf node matches either p or q.
2) If match, then return the node upwards. Otherwise return null.
3) Base case 1: once we reach a node where left and right's upward returns are not null, 
   then we found the common ancestor, no need to backprop anymore.
4) Base case 2: (case where p is also ancestor of q) after propogating to the root node it will have one side as null and one side not null, 
   so we use the not null node as the LCA of both p and q.
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    #80ms ~ O(n) runtime, O(n) >= O(longest depth) memroy
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        #if root:
            #print("root.val: {}".format(root.val))

        #if there's a propagation going on, then keep doing it
        if not root:
            #not an ancestor of p or q, so propogate null upwards
            return None 
        if root==p or root==q:
            #found p/q or is already propagating that value up, so return itself
            return root

        leftProp = self.lowestCommonAncestor(root.left,p,q)
        rightProp = self.lowestCommonAncestor(root.right,p,q)

        #if root:
        #    print("root.val backprop: {}".format(root.val))

        if leftProp and not rightProp:
            #only left child node is an ancestor of p or q
            #print("leftProp: {}".format(leftProp.val))
            return leftProp 
        elif rightProp and not leftProp:
            #only right child node is an ancestor of p or q
            #print("rightProp: {}".format(rightProp.val))
            return rightProp
        elif not leftProp and not rightProp:
            #neither left/right are an ancestor of p,q
            #print("None prop")
            return None
        elif leftProp and rightProp:
            #one children is ancestor of p and another is ancestor of q
            #that means current node is an LCA 
            #print("matching prop")
            return root

from math import ceil
#inputmaker - converts list into binary tree
def listToBinaryTree(inputList) -> TreeNode:
    head = TreeNode(inputList[0],left=None,right=None)
    treeNodeOrder = [] #keep track of treenodes in list so it's easier to link to children
    treeNodeOrder.append(head)
    for i in range(1,len(inputList)):
        if(inputList[i]==None):
            treeNodeOrder.append(TreeNode(-1,left=None,right=None)) #append dummy node, it won't exist in the tree. Only added to array for index mapping.
            continue #skip the rest of linking parent-child
        childNode = TreeNode(inputList[i],left=None,right=None)
        #identify parent node
        parentNode = treeNodeOrder[ceil(i/2)-1]
        #link parent node to child
        if(i%2):
            parentNode.left = childNode
        else:
            parentNode.right = childNode
        treeNodeOrder.append(childNode)
    #print("treeNodeArrLen: {}".format(len(treeNodeOrder)))
    return head

def dfsprint(node:'TreeNode'):
    if not node:
        #print("not node")
        return 
    print("Current Node {} with val: {}".format(node,node.val))
    
    left = node.left
    right = node.right 

    #print("going left")
    dfsprint(left)
    #print("going right")
    dfsprint(right)
    return

def main():
    
    null = None
    root = [3,5,1,6,2,0,8,null,null,7,4]
    p,q = 5, 1 #3 
    print("Input: root={0},p={1},q={2}".format(root,p,q))
    root = listToBinaryTree(root)
    p = root.left 
    q = root.right


    inputs = []
    
    testingOneInput = True
    if testingOneInput:
        #Test single input
        
        #dfsprint(root)
        solution = Solution()
        output = solution.lowestCommonAncestor(root,p,q)
        print("Output: node = {0} with value = {1}".format(output,output.val))
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
