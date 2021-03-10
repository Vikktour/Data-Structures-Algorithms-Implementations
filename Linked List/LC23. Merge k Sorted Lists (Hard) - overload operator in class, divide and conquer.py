"""
Victor Zheng
01-13-2021
23. Merge k Sorted Lists (Hard)
""" 

# Definition for singly-linked list.
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
"""
"""
Approach1: Let N be total number of nodes. O(Nlogk) runtime, O(N) space. 196ms,20.1MB.
Conquer: merge two lists two at a time. 
"""
from typing import List
"""
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:

        if not lists:
            return None

        def merge2Lists(l1,l2) -> ListNode:
            pointer = retHead = ListNode()
            while l1 or l2:
                if l1:
                    v1 = l1.val
                else:
                    v1 = float("inf")
                    
                if l2:
                    v2 = l2.val
                else:
                    v2 = float("inf")
                
                if v1 < v2:
                    pointer.next = ListNode(v1)
                    pointer = pointer.next
                    l1 = l1.next
                else:
                    pointer.next = ListNode(v2)
                    pointer = pointer.next
                    l2 = l2.next
            return retHead.next
        
        #merging list m and n into m repeatedly is too slow. Have to merge each 2 smaller lists together at a time.
        
        # #bad merge - O(N*k)
        # while len(lists) > 1:
        #     #merge the last two lists and pop last one
        #     lists[-2] = merge2Lists(lists[-2],lists[-1])
        #     lists.pop()
        
        #good merge - O(N*log(k))
        while len(lists) > 1:
            mergedLists = []
            #merge each pair of lists and store them in mergedList
            for i in range(0,len(lists),2):
                j = i + 1
                if j < len(lists):
                    mergedLists.append(merge2Lists(lists[i],lists[j]))
                else:
                    #i is a single linked list
                    mergedLists.append(lists[i])
            lists = mergedLists

        return lists[0]
"""

"""
Approach2: O(N*logk) runtime, O(1) extra space - 120ms, 17.5MB
Divide and Conquer

#previous error (now fixed) - O(n) extra space for listnode (I wasn't able to do it without cloning bc when I tried, there was an infinite loop back to self) - 168ms, 18.4MB
"""
"""
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return None 

        def mergeDaQ(lists,start,end) -> ListNode:
            #base case
            if start == end:
                return lists[start]
            
            #divide
            mid = (start + end) // 2
            l1 = mergeDaQ(lists,start,mid)
            l2 = mergeDaQ(lists,mid+1,end)

            #conquer
            pointer = dummyHead = ListNode()
            while l1 and l2:
                if l1.val < l2.val:
                    pointer.next = l1 
                    #pointer.next = ListNode(l1.val)
                    l1 = l1.next 
                else:
                    pointer.next = l2 
                    #pointer.next = ListNode(l2.val)
                    l2 = l2.next 
                pointer = pointer.next
            #l1 and/or l2 depleted, link the rest
            if l1:
                pointer.next = l1
            elif l2:
                pointer.next = l2

            return dummyHead.next 
        
        return mergeDaQ(lists,0,len(lists)-1)
"""

"""
Approach3: Let N=#nodes, O(Nlogk) runtime, O(k) memory - 104ms(68%), 17.9MB(58.5%)
Use minheap to store each linkedlist.
This is for Daily LC problem - 01-24-2021
Learned from Larry: https://www.youtube.com/watch?v=gIIPL0JsvVQ&t=43s&ab_channel=ProgrammingLivewithLarry
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    #include operator overload for less than to allow usage in heap. If we don't use this, we can also do setattr() inside class Solution
    #def __lt__(self,other):
    #    return self.val < other.val

import heapq
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        #overload the "<" operator for ListNode
        
        #setattr(ListNode, "__lt__", lambda self, other: self.val < other.val) #since LC doesn't let us modify ListNode class outside of class Solution, we have to set attribute inside solution
        
        #another method for overloading "<" operator in listnode
        def lt(self:ListNode, other:ListNode) -> bool:
            return True 
        ListNode.__lt__ = lt
        
        pq = []

        #add (frontvalue,Node) for each linkedlist
        for LL in lists:
            if LL:
                heapq.heappush(pq,(LL.val,LL)) #could also use lists index instead of LL, to avoid need to do class operator overload
        
        #pop from list and link nodes together
        head = ListNode()
        current = head
        while pq:
            #add current smallest node to our result list
            _, smallestNode = heapq.heappop(pq)
            current.next = smallestNode
            current = current.next 

            #add back smallest node's next to the minheap
            if smallestNode.next:
                heapq.heappush(pq,(smallestNode.next.val,smallestNode.next))
            
        return head.next


        
            

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

def main():
    
    input = [listToLinkedList([1,4,5]),listToLinkedList([1,3,4]),listToLinkedList([2,6])] #[1,1,2,3,4,4,5,6]
    #input = []
    #input = [listToLinkedList([])]
    #input = [listToLinkedList([]),listToLinkedList([1])] #1

    inputs = []
    
    testingOneInput = True
    if testingOneInput:
        #Test single input
        print("Input: {}".format(input))

        solution = Solution()
        output = solution.mergeKLists(input)
        output = linkedListToList(output)
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



"""
#My accepted solution - O(NlogN) 88ms, 18.4MB
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:

        #put all list of listnodes' values into one list
        values = []
        for aListNode in lists:
            while(aListNode):
                values.append(aListNode.val)
                aListNode = aListNode.next

        #edgecase - empty input
        if values == []:
            return None
        
        #print("values: {}".format(values))
        #sort the list
        values.sort()
        #print("sorted values: {}".format(values))

        #Make a linked list with the sorted values
        head = ListNode()
        temp = head
        for v in values:
            temp.next = ListNode(v)
            temp = temp.next
        
        return head.next
"""

"""
#Divide and Conquer solution (splitting at midpoints then combine)
#Java solution - https://leetcode.com/problems/merge-k-sorted-lists/discuss/10917/Simple-Java-solution-using-binary-searchquite-straightforward
public ListNode mergeKLists(ListNode[] lists) {
    if(lists.length==0)return null;
    int start=0;
    int end=lists.length-1;
    ListNode head=merge(lists,start,end);
    return head;
}

private ListNode merge(ListNode[] lists, int start, int end){
    if(start==end)return lists[start];
    int mid=(start+end)/2;
    ListNode l1=merge(lists,start,mid);
    ListNode l2=merge(lists,mid+1,end);
    ListNode dummy=new ListNode(0);
    ListNode cur=dummy;
    while(l1!=null&&l2!=null){
        if(l1.val>=l2.val){
            cur.next=l2;
            l2=l2.next;
        }else{
            cur.next=l1;
            l1=l1.next;
        }
        cur=cur.next;
    }
    if(l1==null){
        cur.next=l2;
    }
    if(l2==null){
        cur.next=l1;
    }
    return dummy.next;
}
"""





# #Old - 10/30/2020
# """
# 23. Merge k Sorted Lists (Hard)

# """
# Approach: Using min heap

# Sources: 
# Techniques - https://www.geeksforgeeks.org/merge-k-sorted-linked-lists/
# Min heap tree creation and value retrieval - https://www.youtube.com/watch?v=NCuaebwQLKU&ab_channel=WeTeach_CS
# """

# #python 3.9 #for earlier versions of python 3, just change all instances of "list[" into "List["
# import math #for ceiling function
# import copy #for making deep copies of list[list] (helpful for input display)

# #Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
        
# class Solution:
#     def mergeKLists(self, lists: list[ListNode]) -> ListNode:

#         #edgecase - empty list
#         if ( (lists == []) or (lists == [None]) ):
#             return None
        
#         #start by adding first linked-list to the min heap, and then do it for the other lists
#         heap = []
#         #insert first element to heap to make it easier later on (helps avoid having to check if heap is empty every loop)
#         for i,link in enumerate(lists):
#             if(link == None):
#                 continue
#             else:
#                 heap.append(link.val)
#                 lists[i] = lists[i].next
#                 heapLen = 1 #keep track of heap length (don't want to keep calling len())
#                 break
#         for link in lists:
            
#             #iterate through this linked list and append to heap list
#             while(link != None):
                
#                 curVal = link.val
#                 heap.append(curVal)
#                 heapLen += 1
#                 curIdx = heapLen-1
#                 parentIdx = math.ceil(curIdx)-1
                
#                 #check if curVal is less than parent
#                 if(curVal < heap[parentIdx]):
#                     #heapify
#                     self.heapify(heap,heapLen)
                
#                 link = link.next
        
#         #print("heap before sorting: {}".format(heap))

#         #Now that we have a complete minheap tree, we can start creating a linked list with sorted values
#         sortedList = self.heapToSortedList(heap)

#         return sortedList

#     #heapify takes the most recently inserted number and bubble up to correct the minheap (i.e. if the most recent number is < parent node then keep swapping upwards)
#     def heapify(self,heap:list[int],heapLen:int) -> list[int]:
        
#         #heapLen = len(heap) #avoid adding unecessary O(N)
#         curIdx = heapLen-1
#         curVal = heap[curIdx]
#         parentIdx = math.ceil(curIdx)-1

#         while(curVal < heap[parentIdx]):
#             #bubble up (swap values of parent and child)
#             temp = heap[parentIdx]
#             heap[parentIdx] = curVal 
#             heap[curIdx] = temp

#             #update indices
#             curIdx = parentIdx
#             if(curIdx == 0):
#                 return heap #curVal is at the top, so can no longer move upwards
#             parentIdx = math.ceil(curIdx)-1

#             #print("heap in heapify: {}".format(heap))

#         return heap
    
#     #this function will remove the root node (which is the min value), then replace it with the last node
#     #the last node is then heapified downwards until the min heap is valid again
#     def heapToSortedList(self,heap:list[int]) -> ListNode:

#         head = ListNode() #start out with a dummy head, will remove it later
#         tempPointer = head
#         heapLen = len(heap)

#         while(heap):
#             #print("heap in heapToSortedList: {}".format(heap))
#             #replace the root node with the last element on list
#             tempPointer.next = ListNode(heap[0])
#             tempPointer = tempPointer.next
#             curVal = heap[heapLen-1]
#             heap[0] = curVal
#             heap.pop()
#             heapLen -= 1
#             curIdx = 0
#             noMoreChild = False

#             ##bubble down the root node to fix the min heap
#             child1Idx = curIdx * 2 + 1
#             child2Idx = curIdx * 2 + 2
#             if(child1Idx > heapLen-1):
#                 #we're done bubbling down
#                 noMoreChild = True
#             elif(child2Idx > heapLen-1): #there's a first child but no second child
#                 minChildIdx = child1Idx
#             elif(heap[child1Idx] <= heap[child2Idx]):
#                 minChildIdx = child1Idx
#             else:
#                 minChildIdx = child2Idx

#             if(noMoreChild):
#                 pass
#             else:
#                 minChildVal = heap[minChildIdx]
#                 #swap parent and child until min heap is valid
#                 while( (curVal > minChildVal) and (not noMoreChild) ):
                    
#                     temp = heap[curIdx]
#                     heap[curIdx] = minChildVal
#                     heap[minChildIdx] = temp 

#                     curIdx = minChildIdx
#                     child1Idx = curIdx * 2 + 1
#                     child2Idx = curIdx * 2 + 2
#                     if(child1Idx > heapLen-1):
#                         #we're done bubbling down
#                         noMoreChild = True
#                         break
#                     elif(child2Idx > heapLen-1): #there's a first child but no second child
#                         minChildIdx = child1Idx
#                     elif(heap[child1Idx] <= heap[child2Idx]):
#                         minChildIdx = child1Idx
#                     else:
#                         minChildIdx = child2Idx
#                     minChildVal = heap[minChildIdx]

#         #Remove the dummy head node
#         tempPointer = head
#         head = head.next 
#         tempPointer = None 

#         return head

# #I make this function to make it easier for creating inputs / testing sample cases
# def inputMaker(lists:list[list[int]]) -> list[ListNode]:
#     retList = []
#     for aList in lists:
#         head = ListNode()
#         temp = head
#         lenList = len(aList)
#         if(lenList == 0):
#             retList.append(None)
#             continue
#         #keep adding node links until the list is empty
#         while(lenList>0):
#             temp.next = ListNode(aList[0])
#             temp = temp.next
#             #print("inserting {} to linked-list: ".format(aList[0]))
#             aList.pop(0)
#             lenList -=1
        
#         #remove dummy head node
#         temp = head
#         head = head.next
#         temp = None
#         retList.append(head)

#         # #verify by printing out list:
#         # print("------------------printing linked list------------------")
#         # while(head != None):
#         #     print("linkedlistval: {}".format(head.val))
#         #     head = head.next
#     return retList

# #I make this function to print output in list form
# #Converts a linked-list into list
# def outputMaker(head:ListNode) -> list[int]:

#     retList = []
#     while(head != None):
#         retList.append(head.val)
#         head = head.next
    
#     return retList



# def main():

#     # #example 1
#     # inputArray = []
#     # input = copy.deepcopy(inputArray)
#     # input = inputMaker(input) #output []

#     # #example 2
#     # inputArray = [[],[]]
#     # input = copy.deepcopy(inputArray)
#     # input = inputMaker(input) #output []

#     #example 3
#     inputArray = [[1,3,5],[],[2,5,7]]
#     input = copy.deepcopy(inputArray)
#     input = inputMaker(input) #output [1,2,3,5,5,7]

#     #example 3.1
#     inputArray = [[],[1,3,5],[2,5,7]]
#     input = copy.deepcopy(inputArray)
#     input = inputMaker(input) #output [1,2,3,5,5,7]


#     #example 4
#     # inputArray = [[1,4,5],[1,3,4],[2,6]]
#     # input = copy.deepcopy(inputArray)
#     # #print("input: {}".format(input))
#     # input = inputMaker(input) #output [1,1,2,3,4,4,5,6]
    
#     #testpring first list of inputMaker
#     #print("input from inputMaker: {}".format(input))
#     #print("input list[0]: {}".format(outputMaker(input[0])))
#     #print("input first list first val: {}".format(input[0].val))

#     solution = Solution()
#     output = solution.mergeKLists(input)
#     outputListForm = outputMaker(output)
#     print("InputArray: {0}".format(inputArray))
#     print("outputListForm: {0}".format(outputListForm))

# if __name__ == main():
#     main()



# """
# #Approach 2: using brute force sorting and creating linked list
# #this turned out to be 92ms,18.1MB as opposed to my previous solution's 7544ms,18.2MB

# #python 3.9 #for earlier versions of python 3, just change all instances of "list[" into "List["
# import math #for ceiling function   
# import copy #for making deep copies of list[list] (helpful for input display)

# #Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
        
# class Solution:
#     def mergeKLists(self, lists: list[ListNode]) -> ListNode:

#         #put all list of listnodes' values into one list
#         values = []
#         for aListNode in lists:
#             while(aListNode):
#                 values.append(aListNode.val)
#                 aListNode = aListNode.next

#         #edgecase - empty input
#         if values == []:
#             return None
        
#         #print("values: {}".format(values))
#         #sort the list
#         values.sort()
#         #print("sorted values: {}".format(values))

#         #Make a linked list with the sorted values
#         head = ListNode()
#         temp = head
#         for v in values:
#             temp.next = ListNode(v)
#             temp = temp.next
        
#         return head.next

# """