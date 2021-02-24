"""
Victor Zheng
12-30-2020
138. Copy List with Random Pointer (Medium)
""" 
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

"""
Approach2: ~O(n) runtime and space. Use a dictionary to hash original node to original index, and have a list to store all of the copied nodes in order.
Then loop through both lists and for each original node, find it's random index using dictionary and then use the copylist and randomindex to link
copynode to copynode's random.
"""
"""
class Solution:
    #28ms ~ O(n) runtime, O(n) memory
    def copyRandomList(self, head: 'Node') -> 'Node':
        
        origCurrent = head
        if not origCurrent:
            return None

        origToOrigIndex = {}
        #originalToRandomIndex can be acquired from original --> random --> index
        copyArr = [] #stores the copy nodes in order

        copyPointer = Node(0) #dummy head
        copyCurrent = copyPointer
        #iterate through original and create copy linked list. Fill up dictionaries.
        index = 0
        while origCurrent:

            #create copy
            copyCurrent.next = Node(origCurrent.val)
            copyCurrent = copyCurrent.next
            copyArr.append(copyCurrent)

            #append to dictionary
            origToOrigIndex[origCurrent] = index

            origCurrent = origCurrent.next 
            index += 1
        
        
        #reset the current pointers to the start
        origCurrent = head
        copyCurrent = copyPointer.next 
        #iterate through copied linked list and link the randoms
        while copyCurrent:
            
            #get the index of the random
            if origCurrent.random:
                randomIndex = origToOrigIndex[origCurrent.random]
                #assign the random node for copy node
                copyCurrent.random = copyArr[randomIndex]
            #otherwise the random is None
            
            origCurrent = origCurrent.next
            copyCurrent = copyCurrent.next 
        
        return copyPointer.next 
"""
"""
Approach3: O(n) runtime and O(1) space. Rewire the original input to zigzag along with the copy list.
Idea: https://www.youtube.com/watch?v=OvpKeraoxW0&ab_channel=BackToBackSWE
Ex: 
orig1 orig2 orig3 orig4
copy1 copy2 copy3 copy4

1st pass: Clone and rewire
orig1.next = copy1, copy1.next = orig2, orig2.next = copy2, ...

2nd pass: Assign random
so now we can say that copy1.random = orig1.random.next

3rd pass: Separate the linked list
after we are done setting up the randoms, we need to make them two separate linked lists.
"""

#POSTSUBMIT COMMENT: I'm not sure why this is 15.2MB memory while the above solution is 14.9MB memory.
class Solution:
    #36ms ~ O(n) runtime, O(1) memory
    def copyRandomList(self, head: 'Node') -> 'Node':
        
        if not head:
            return None

        #1st pass: create copy nodes and link orig&copy in zigzag
        origNode = head
        #copyNode = Node(0) #dummy head node
        while origNode:
            
            copyNode = Node(origNode.val)
            nextOrig = origNode.next 
            
            #zigzag link
            origNode.next = copyNode 
            copyNode.next = nextOrig 
            
            #move pointer forward
            origNode = nextOrig 
        
        #2nd pass: assign random for each copyNode
        #print("2nd pass -----")
        origNode = head 
        while origNode:
            #print("val: {}".format(origNode.val))
            copyNode = origNode.next 

            origRandom = origNode.random
            if origRandom:
                copyNode.random = origRandom.next 
            
            origNode = origNode.next.next 
        
        #3rd pass: separate the zigzag into two separate linked lists
        #print("3rd pass -----")
        origNode = head 
        copyHead = origNode.next #the head of copy linked list. We will return this
        copyNode = copyHead
        while origNode:
            #print("val: {}".format(origNode.val))
            nextOrig = origNode.next.next 
            
            if nextOrig:
                origNode.next = nextOrig 
                copyNode.next = nextOrig.next 
                origNode = nextOrig
                copyNode = copyNode.next
            else:
                #no more next nodes
                break
        return copyHead

"""
Approach4: O(N) runtime O(N) space
Two pass instead of three pass.
1) Create copy nodes and link all orig nodes to point to respective copy node. Temporarily set copy node's random pointer to point to random node's random
2) Link copy node's random pointer to point to orig node's random.next (note that our copynode.random is orignode.random, so we just set copynode.random to copynode.random.next)
Idea from: https://leetcode.com/problems/copy-list-with-random-pointer/discuss/1059384/Python-O(n)-time-O(1)-space-two-passes
Diagram: https://drive.google.com/file/d/1dMgZiphyBVx_nJiwOPDq0lSr4PBe1_QP/view?usp=sharing
"""

def main():
    
    input = ""

    inputs = []
    
    testingOneInput = True
    if testingOneInput:
        #Test single input
        print("Input: {0}".format(input))

        solution = Solution()
        output = solution.func(input)
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


"""
#FAILED APPROACH - It is going to be O(n^2) when I try mapping different set() together.
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        
        curPointer = head
        if not curPointer:
            return None
        
        copyList = Node() #dummy head
        copyPointer = copyList
        
        #First create a linked list with just next pointers (set all random to none)
        #Append all nodes to a list so we can create an easy linking to randomIdx
        #As we iterate original linked list, store dictionary: dict[index] = randomIndex
        copyNodesList = []
        originalNodeToRandomIndex = {}
        randomIndexTo
        index = 0
        while curPointer != None:
            copyPointer.next = Node(curPointer.val)
            copyNodesList.append(copyPointer)
            nodeToRandom[index] = #THIS DOESN'T WORK
            copyPointer = copyPointer.next
"""


"""
#2-10-2021 Daily Problem - I did it in two ways again for practice
Approach1: O(N) runtime O(N) space - 32ms, 15.1MB
Use dictionary to map original node to cloned node (so each time we create a copy node, the random node will be the original node's random node's lookup to copy node)
"""
"""
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        origToCopy = {} #map each orig node its respective copy node
        
        copyHead = Node(-1) #dummy head node 
        copyCur = copyHead
        cur = head
        
        #do iteration to create copyList without the randoms first (so we can fill up the dictionary)
        while cur:
            copyCur.next = Node(cur.val)
            
            #map new node pair, and advance the pointers
            origToCopy[cur] = copyCur.next
            cur = cur.next
            copyCur = copyCur.next
        
        #iterate through linked list again and now assign random pointers
        cur = head
        copyCur = copyHead
        while cur:
            #get the copyRandom
            origRandom = cur.random
            if origRandom:
                copyRandom = origToCopy[origRandom]
            else:
                copyRandom = None
                
            #assign the random pointer
            copyCur.next.random = copyRandom
            
            #advance the pointers
            cur = cur.next
            copyCur = copyCur.next
            
        return copyHead.next
"""
"""
#2-10-2021 Daily Problem - I did it in two ways again for practice
Approach2: O(N) runtime, O(N) space (but a bit better without the dictionary - O(1) if you don't count the Copy Linked List) - 36ms, 15.1MB
zigzag approach - link next of orig to copy to orig to copy (in zigzag fashion)
Then assign the random pointers of copy to orig's random.next
Then split up to two linked lists
"""
"""
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        
        cur = head
        copyHead = Node(-1)
        copyCur = copyHead
        
        #create copy list and use zigzag order
        while cur:
            copyCur.next = Node(cur.val)
            nextCur = cur.next
            cur.next = copyCur.next
            copyCur.next.next = nextCur
            cur = nextCur
        #verifying that zigzag worked
        #cur = head
        #while cur:
        #    print(cur.val)
        #    cur = cur.next
        
        #connect the randoms
        cur = head
        while cur:
            #The random is either None or exists
            if cur.random:
                #random is not None so set copy.random to orig.random.next
                cur.next.random = cur.random.next
            #if it's None then we don't have to do anything bc copy.random is none by default
                
            cur = cur.next.next
        
        #split up into two linked lists
        cur = head
        copyCur = copyHead
        while cur:
            copyCur.next = cur.next
            cur = cur.next.next
            copyCur = copyCur.next           
        
        return copyHead.next
"""