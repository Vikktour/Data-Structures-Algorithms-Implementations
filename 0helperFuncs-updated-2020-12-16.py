"""
Victor Zheng
Last updated - 2020-12-16
Helper functions to help generate input/output/prints for particular Leetcode problems. This is useful when trying to run/debug locally.
For example, some of these functions can be used to help structure the input to turn a list into a linked list.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
from math import ceil
#inputmaker - converts list into binary tree
#note: set null = None for input with variable null (e.g. [1,2,3,null,4,5,null], that way null is defined as None)
def listToBinaryTree(inputList) -> TreeNode:
    if len(inputList) == 0:
        return None
    head = TreeNode(inputList[0])
    treeNodeOrder = [] #keep track of treenodes in list so it's easier to link to children
    treeNodeOrder.append(head)
    for i in range(1,len(inputList)):
        #if(inputList[i]=="null"):
        if(inputList[i]==None):
            treeNodeOrder.append(TreeNode()) #append dummy node, it won't exist in the tree. Only added to array for index mapping.
            continue #skip the rest of linking parent-child
        childNode = TreeNode(inputList[i])
        #identify parent node
        parentNode = treeNodeOrder[ceil(i/2)-1]
        #link parent node to child
        if(i%2):
            parentNode.left = childNode
        else:
            parentNode.right = childNode
        treeNodeOrder.append(childNode)
    return head

class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
#read out rows of perfect binary tree (e.g. put first row into array, then second row into array, then third, etc...)
def perfectBinaryTreeReadRows(root:Node):
    retList = []
    leftMostNode = curNode = root
    while(curNode):
        retList.append(curNode.val)
        curNode = curNode.next
        #at the last adjacent node, now move pointer to beginning of leftmost child
        if(not curNode):
            retList.append("#")
            curNode = leftMostNode.left
            leftMostNode = leftMostNode.left
    return retList

#read out rows of any binary tree (e.g. put first row into array, then second row into array, then third, etc...)
def binaryTreeReadRows(root:Node):
    retList = []
    curNode = root

    leftMostChildNodeDiscovered = False
    while(curNode):
        retList.append(curNode.val)
        if not leftMostChildNodeDiscovered:
            if curNode.left:
                leftMostChildNodeDiscovered = True 
                leftMostChildNode = curNode.left 
            elif curNode.right:
                leftMostChildNodeDiscovered = True 
                leftMostChildNode = curNode.right 
        curNode = curNode.next
        #at the last adjacent node, now move pointer to beginning of leftmost child
        if(not curNode):
            retList.append("#")
            if not leftMostChildNodeDiscovered:
                break
            curNode = leftMostChildNode
            leftMostChildNodeDiscovered = False

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import List
#helper function to convert list into proper linked-list input
def listToLinkedList(listInts: List[int]) -> ListNode:
    head = ListNode()
    temp = head
    while(listInts):
        temp.next = ListNode(listInts[0])
        listInts.pop(0)
        temp = temp.next
    return head.next
#converts linked list to list
def linkedListToList(head:ListNode) -> List[int]:
    retList = []
    while(head):
        retList.append(head.val)
        head = head.next
    return retList

#converts list of list of int into list of Listnode
from typing import List
def inputMaker(lists:List[List[int]]) -> List[ListNode]:
    retList = []
    for aList in lists:
        head = ListNode()
        temp = head
        lenList = len(aList)
        if(lenList == 0):
            retList.append(None)
            continue
        #keep adding node links until the list is empty
        while(lenList>0):
            temp.next = ListNode(aList[0])
            temp = temp.next
            #print("inserting {} to linked-list: ".format(aList[0]))
            aList.pop(0)
            lenList -=1
        
        #remove dummy head node
        temp = head
        head = head.next
        temp = None
        retList.append(head)

        # #verify by printing out list:
        # print("------------------printing linked list------------------")
        # while(head != None):
        #     print("linkedlistval: {}".format(head.val))
        #     head = head.next
    return retList



# (1656. Design an Ordered Stream (Easy)). Similar to 5560. Design Front Middle Back Queue (Medium).
# Other problems: 173 (TreeNode), 
# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(id,value)
class OrderedStream:
    def __init__(self, n: int):
        self.n = n
    def insert(self, id: int, value: str) -> List[str]:
        return ["0"]

#class implementation (more generalized) - take in inputs with function name and arguments - do the operations
#evaluate the method - https://www.kite.com/python/answers/how-to-call-a-function-by-its-name-as-a-string-in-python
#using ' to put string inside string: https://stackoverflow.com/questions/9050355/using-quotation-marks-inside-quotation-marks 
def classTesting(names:List[str],args):
    retList = []

    classInitializer = names[0]
    arg = args[0]
    if len(arg) > 0:
        argument = "("
        nextItem = False
        for item in arg:
            if nextItem:
                argument = argument + "," + "\'" + str(item) + "\'"
            else:
                argument = argument + str(item) #for normal values (e.g. int,bool,etc.)
                #argument = argument + "item" #for user defined class objects (e.g. Node,TreeNode)
                nextItem = True
        argument += ")"
        print("init argument: {}".format(argument)) #swap argument assingment line above if input is a user defined class (e.g. TreeNode) since argument is the object instance and not the name of the object
    else:
        argument = "()"    
    theClass = eval(classInitializer + argument) #call the class to instantiate an object
    retList.append(None)
    
    namesLen = len(names)
    if namesLen <= 1:
        return retList
    
    for index in range(1,namesLen):
        method = names[index]

        #get the arguments
        arg = args[index]
        if arg == []:
            argument = "()"
        else:
            argument = "("
            nextItem = False
            for item in arg:
                if nextItem:
                    argument = argument + "," + "\'" + str(item) + "\'"
                else:
                    argument = argument + str(item)
                    nextItem = True
            argument += ")"

        print("evaluating: {}".format("theClass." + method + argument))
        result = eval("theClass." + method + argument)

        if result == None:
            retList.append("null")
        else:
            retList.append(result)
    
    return retList

#collections library features
import collections
#creates dictionary based on string input (e.g. "apple" --> {a:1,p:2,l:1,e:1})
somestring = "apple"
word1Collection = collections.Counter(somestring)