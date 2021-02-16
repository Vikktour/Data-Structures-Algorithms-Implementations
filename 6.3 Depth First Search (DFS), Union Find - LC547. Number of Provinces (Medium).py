"""
Victor Zheng
02-06-2021
547. Number of Provinces (Medium)
I HAVE TO COME BACK AND ANALYZE RUNTIME, ALSO EXPLAIN ADDEDGE()
""" 
"""
Approach1: O(NlogN) - 196ms (53.56%), 14.6MB (73.48%)
Union Find
https://leetcode.com/problems/number-of-provinces/discuss/152441/Python-Union-Find-solution
Referred to Ghos3t's implementation in the comments. I like the way they implemented union find.
"""
from typing import List
import collections
"""
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        #maps node to height of tree the node is in
        rank = collections.defaultdict(int)
        
        #maps node to parent node
        parent = collections.defaultdict(int)
        
        #Given a node, return the root node. Path compression optimized.
        def findRoot(node:int):
            if parent[node] == node:
                return node
            
            #path compression - link node's parent directly to root
            parent[node] = findRoot(parent[node])
            
            return parent[node]
        
        #Given two nodes (of an edge), merge them into one tree. Union by rank optimized.
        def union(nodeA:int, nodeB:int):
            
            rootA = findRoot(nodeA)
            rootB = findRoot(nodeB)
            
            if rank[rootA] >= rank[rootB]:
                #rootA has longer (or equal) depth, so let rootA be the root of both
                parent[rootA] = rootB
            else:
                #rootB has longer depth, so let rootB be the root of both
                parent[rootB] = rootA
            return
        
        rows = len(isConnected)
        cols = len(isConnected[0])
        result = rows #start out with every node being a province itself
        
        for i in range(rows):
            rank[i] = 1 #initilize rank - each node will have a rank of 1 at the start (i.e. assume everything is separated at the start, until we start unionizing edges)
            parent[i] = i #initialize parent nodes - each node will be their own root at the start
        
        #iterate through matrix (adjacency list)
        for i in range(rows-1):
            for j in range(i+1, cols):
                if i!=j and isConnected[i][j] == 1 and findRoot(i) != findRoot(j):
                    #If this edge is a new merge to another province, then subtract 1 from result
                    union(i,j)
                    result -= 1
        return result
"""

"""
Approach2: O(N^2) runtime, O(N) space for recursive stack - 176ms (97.57%), 15.3MB (10.18%)
DFS - easier to implement
Each row i indicates a connection from i to each item j in row i.
If item is 1, then there's a connection b/w i and j.
We can start with first item, and then recursively traverse that item's row, and continue down that path in DFS manner.
So we started off on row 0, but the nodes connected to i=0 will also be traversed down and we may end up clearing multiple rows
just for the first iteration, which gives us one province. The nodes that we traverse will be stored in visited set() so we don't 
traverse them again. We continue to do it for other rows (new i), as long as it's not visited yet, which will help us find more provinces.

reference video by LC Bear: https://www.youtube.com/watch?v=70Gbi7LYZOM&ab_channel=LCBear
"""
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        N = len(isConnected)
        visited = set()

        def dfs(cityI):
            #cityIConnections is a row in isConnected, which contains the city i's connections
            cityIConnections = isConnected[cityI]
            visited.add(cityI) #add cityI to seen, so we won't dfs it again (because we called it just now!)
            #we want to take all 1's in cityIConnections to put together into a province
            for cityJ in range(N):
                #check cityJ's connections first before finishing cityI's connections
                if (cityJ not in visited) and (cityIConnections[cityJ] == 1) and (cityI != cityJ):
                    dfs(cityJ)
            #we're done searching cityI's direct connections
            return 
        
        numProvinces = 0
        for cityI in range(N):
            #each entire dfs recursion set is going to be one province
            if cityI not in visited:
                dfs(cityI)
                numProvinces += 1
        return numProvinces

def main():
    
    input = [[1,1,0],[1,1,0],[0,0,1]] #2

    expected = ""

    inputs = []
    
    testingOneInput = True
    if testingOneInput:
        #Test single input
        print("Input: {}".format(input))

        solution = Solution()
        output = solution.findCircleNum(input)
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