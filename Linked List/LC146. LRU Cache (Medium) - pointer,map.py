"""
Victor Zheng
11-17-2020
146. LRU Cache (Medium)
"""
"""
Approach1: O(1) runtime for all func, O(N) space - where N is the number of put() calls
Using ordered dict
"""
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
import collections
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = collections.OrderedDict()

    def get(self, key: int) -> int:
        if key in self.cache:
            self.cache.move_to_end(key,last=False) #move key to front of list (LRU is going to be at the end of list)
            return self.cache[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key] = value 
        elif len(self.cache) < self.capacity:
            self.cache[key] = value 
        else: # > capacity 
            #evict least used item, then add new item
            self.cache.popitem() #pop first item (LRU is popped)
            self.cache[key] = value
        self.cache.move_to_end(key,last=False) #move key to front of list (LRU is going to be at the end of list)


from typing import List
def makeLRU(func,params:List[int]) -> None:

    inputLen = len(func)
    lru = LRUCache(params[0][0])
    retList = [None]
    for i in range(1,inputLen):
        if func[i] == "put":
            #print("put: {}".format(params[i]))
            retList.append(lru.put(params[i][0],params[i][1]))
        elif func[i] == "get":
            #print("get: {}".format(params[i]))
            retList.append(lru.get(params[i][0]))
    
    return retList

"""
Approach2:
Adding linked list in dictionary to move element to front in O(1)
https://stackoverflow.com/questions/54808556/what-is-a-time-complexity-of-move-to-end-operation-for-ordereddict-in-python-3
04-10-2021 practice
"""
#THIS IMPLEMENATION HAS ERROR (FOR LAST LONG TEST CASE) - SOMETHING MAY BE WRONG WITH MY USAGE OF LINKED LIST 
"""
class ListNode:
    def __init__(self,key,val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None
        
class LRUCache:

    def __init__(self, capacity: int):
        #head is LRU, tail is MRU
        self.head = None
        self.tail = None
        self.cap = capacity
        self.keyToNode = {}
 
    def get(self, key: int) -> int:
        #print("get {}".format(key))
        if key in self.keyToNode:
            #move the node to MRU (tail)
            node = self.keyToNode[key]
            if node != self.tail:
                if self.head == node:
                    #if node is head then our next node is head
                    if node.next:
                        self.head = node.next
                    else:
                        #there is only 1 node in LL, so no moving necessary
                        return self.keyToNode[key].val
                if node.prev:
                    node.prev.next = node.next
                if node.next:
                    node.next.prev = node.prev
                self.tail.next = node
                self.tail = node
            #return the value
            #print("head key,val: {},{}".format(self.head.key,self.head.val))
            return self.keyToNode[key].val
        else:
            return -1
            

    def put(self, key: int, value: int) -> None:
        #print("put {},{}".format(key,value))
        if key in self.keyToNode:
            #print("here1")
            #this key already exists, so move it to most recently used (tail)
            node = self.keyToNode[key] 
            if node != self.tail:
                #link prev and next
                if node.prev:
                    node.prev.next = node.next
                else:
                    #no prev, so the next node is the head
                    self.head = node.next
                #link next to prev
                node.next.prev = node.prev
                
                #link node to tail
                self.tail.next = node
                node.prev = self.tail
                self.tail = node
            #update the value for this key
            node.val = value
        else:
            #print("here2")
            #key doesn't exist, add it
            node = ListNode(key,value)
            if len(self.keyToNode) == self.cap:
                #capacity is full, get rid of LRU (head), and attach new node to MRU (tail)
                nodeToRemove = self.head
                if len(self.keyToNode) == 1:
                    #cap of 1 - delete node and make new node
                    self.head = self.tail = node
                else:
                    #more than 1 node
                    self.head = self.head.next
                    self.head.prev = None
                    self.tail.next = node
                    self.tail = node
                    #print("head={},tail={}".format(self.head,self.tail))
                del self.keyToNode[nodeToRemove.key]
                del nodeToRemove
            else:
                #capacity not full yet add new node to MRU (tail)
                if len(self.keyToNode) == 0:
                    #no nodes yet
                    self.head = self.tail = node
                else:
                    #there's at least one node, attach to end
                    self.tail.next = node
                    node.prev = self.tail
                    self.tail = node
            self.keyToNode[key] = node
        #print("keyToNode: {}".format(self.keyToNode))
        #if self.head:
        #    print("head key,val: {},{}".format(self.head.key,self.head.val))
"""
#I fiex the above implementation after many hours ofd ebugging
class ListNode:
    def __init__(self,key,val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

#for debugging
def printLL(node):
    #arr = []
    count = 0
    while node != None:
        if count == 10: break
        #count += 1
        #arr.append((node.key,node.val))
        print((node.key,node.val),end=" ")
        node = node.next
    print("")
    #print(arr)
    return

class LRUCache:

    def __init__(self, capacity: int):
        #head is LRU, tail is MRU
        self.head = None
        self.tail = None
        self.cap = capacity
        self.keyToNode = {}

    def get(self, key: int) -> int:
        #print("get {}".format(key))
        if key in self.keyToNode:
            #move the node to MRU (tail)
            node = self.keyToNode[key]
            if node != self.tail:
                if node == self.head:
                    #if node is head then make our next node be new head, and make it's prev None
                    if node.next:
                        self.head = node.next 
                        #node.prev = None #done later one by linking next to prev
                    #else: #won't reach here bc node != self.tail
                        #there is only 1 node in LL, so no moving necessary
                        #return self.keyToNode[key].val
                #link the node's left and right        
                if node.prev:
                    #if node.next: #don't have to check this bc it would mean the node is at tail already
                    node.prev.next = node.next
                    #else: #don't need this else since here's guaranteed to be a next (since  node != tail)
                        #no next, so it will link to node
                        #print("no next")
                if node.next:
                    node.next.prev = node.prev
                    
                #move node to tail
                self.tail.next = node
                node.prev = self.tail
                node.next = None
                self.tail = node
                
            #return the value
            #printLL(self.head)
            #print("head key,val: {},{}".format(self.head.key,self.head.val))
            return self.keyToNode[key].val
        else:
            return -1
            

    def put(self, key: int, value: int) -> None:
        #print("put {},{}".format(key,value))
        #if self.head:
        #    print("head: {},{}".format(self.head.key,self.head.val))
        if key in self.keyToNode:
            #print("here1")
            #this key already exists, so move it to most recently used (tail)
            node = self.keyToNode[key] 
            #print("node: v={},p={},n={}".format(node.val,node.prev,node.next))
            if node != self.tail:
                #link prev and next
                if node.prev:
                    node.prev.next = node.next
                else:
                    #no prev, so the next node is the head
                    self.head = node.next
                #link next to prev
                node.next.prev = node.prev
                
                #link node to tail
                self.tail.next = node
                node.prev = self.tail
                node.next = None
                self.tail = node
            #update the value for this key
            node.val = value
        else:
            #print("here2")
            #key doesn't exist, add it
            node = ListNode(key,value)
            if len(self.keyToNode) == self.cap:
                #capacity is full, get rid of LRU (head), and attach new node to MRU (tail)
                nodeToRemove = self.head
                if len(self.keyToNode) == 1:
                    #cap of 1 - delete node and make new node
                    self.head = self.tail = node
                else:
                    #more than 1 node
                    self.head = self.head.next
                    self.head.prev = None
                    self.tail.next = node
                    node.prev = self.tail
                    self.tail = node
                    #print("head={},tail={}".format(self.head,self.tail))
                #print("dict: {}".format([key for key in self.keyToNode]))
                #print("deleting {} from dict".format(nodeToRemove.key))
                del self.keyToNode[nodeToRemove.key]
                del nodeToRemove
            else:
                #capacity not full yet add new node to MRU (tail)
                if len(self.keyToNode) == 0:
                    #no nodes yet
                    self.head = self.tail = node
                else:
                    #there's at least one node, attach new node to end
                    self.tail.next = node
                    node.prev = self.tail
                    self.tail = node
            #print("adding {} to dict".format(key))
            self.keyToNode[key] = node
        #print("keyToNode: {}".format(self.keyToNode))
        #if self.head:
        #    printLL(self.head)
            #print("head key,val: {},{}".format(self.head.key,self.head.val))

def main():

    input1 = ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
    input2 = [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]] #[null, null, null, 1, null, -1, null, -1, 3, 4]

    input1 = ["LRUCache","put","put","put","put","get","get"]
    input2 = [[2],[2,1],[1,1],[2,3],[4,1],[1],[2]] #[null,null,null,null,null,-1,3]

    input1 = ["LRUCache","put","put","get","put","get","put","get","get","get"]
    input2 = [[2],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]] #[null,null,null,1,null,-1,null,-1,3,4]

    """
    ["LRUCache","put","put","put","put","get","get"]
[[2],[2,1],[1,1],[2,3],[4,1],[1],[2]]
["LRUCache","put","put","get","put","put","get"]
[[2],[2,1],[2,2],[2],[1,1],[4,1],[2]]
["LRUCache","put","put","get","put","get","put","get","get","get"]
[[2],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]
["LRUCache","put","put","put","put","get","get"]
[[2],[2,1],[1,1],[2,3],[4,1],[1],[2]]
["LRUCache","put","put","put","put","put","get","put","get","get","put","get","put","put","put","get","put","get","get","get","get","put","put","get","get","get","put","put","get","put","get","put","get","get","get","put","put","put","get","put","get","get","put","put","get","put","put","put","put","get","put","put","get","put","put","get","put","put","put","put","put","get","put","put","get","put","get","get","get","put","get","get","put","put","put","put","get","put","put","put","put","get","get","get","put","put","put","get","put","put","put","get","put","put","put","get","get","get","put","put","put","put","get","put","put","put","put","put","put","put"]
[[10],[10,13],[3,17],[6,11],[10,5],[9,10],[13],[2,19],[2],[3],[5,25],[8],[9,22],[5,5],[1,30],[11],[9,12],[7],[5],[8],[9],[4,30],[9,3],[9],[10],[10],[6,14],[3,1],[3],[10,11],[8],[2,14],[1],[5],[4],[11,4],[12,24],[5,18],[13],[7,23],[8],[12],[3,27],[2,12],[5],[2,9],[13,4],[8,18],[1,7],[6],[9,29],[8,21],[5],[6,30],[1,12],[10],[4,15],[7,22],[11,26],[8,17],[9,29],[5],[3,4],[11,30],[12],[4,29],[3],[9],[6],[3,4],[1],[10],[3,29],[10,28],[1,20],[11,13],[3],[3,12],[3,8],[10,9],[3,26],[8],[7],[5],[13,17],[2,27],[11,15],[12],[9,19],[2,15],[3,16],[1],[12,17],[9,1],[6,19],[4],[5],[5],[8,1],[11,7],[5,2],[9,28],[1],[2,2],[7,4],[4,22],[7,24],[9,26],[13,28],[11,26]]
    """
    print("Input: func:{0}, params:{1}".format(input1,input2))

    output = makeLRU(input1,input2)
    print("Output: {0}".format(output))

if __name__ == main():
    main()