"""
Victor Zheng
01-24-2021
675. Cut Off Trees for Golf Event (Hard)
Discussion: https://leetcode.com/problems/cut-off-trees-for-golf-event/discuss/1033258/Python-BFS-and-PriorityQueue-with-comments-and-print-for-visualization
""" 
"""
Complexity:
Let m=len(forest), n=len(forest[0])
O(mn*log(mn) + 3^(m+n)) runtime - 692ms (45.50%)
O(m*n) space - 14.9MB (56.88%)

Approach: 
Have priority queue that stores (height,x,y) for each tree in order of min to max.
Use BFS to find the next available smallest height in priority queue.
"""

from typing import List 
import heapq
import collections
import numpy as np #for printing
class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        #print("forest at start: \n{}".format(np.array(forest)))
        m = len(forest)
        n = len(forest[0])
        
        #store all trees in priority queue in (height,x,y) format
        pq = []
        for x in range(m):
            for y in range(n):
                height = forest[x][y]
                if height > 1:
                    heapq.heappush(pq,(height,x,y))
        #print("heap: {}".format(pq))
        
        #takes in starting position and next tree position, returns min steps to get to that next tree position
        def bfs(x,y,nextX,nextY) -> int:
            queue = collections.deque([(x,y,0)])
            seen = {(x,y)}
            #print("starting at: ({},{})".format(x,y))
            #keep BFS searching until we find target tree or tried all paths
            while queue:
                x,y,steps = queue.popleft()

                if x == nextX and y == nextY:
                    #found the next tree, chop it down and return depth
                    forest[x][y] = 1
                    #print("ending at: ({},{}) after {} steps".format(x,y,steps))
                    return steps

                #append adjacent nodes (if they are a valid position i.e. height >= 1, within bounds of forest, and not already used)
                for dx,dy in [(-1,0),(0,1),(0,-1),(1,0)]:
                    adjX,adjY = x+dx, y+dy
                    if (0 <= adjX < m and 0 <= adjY < n) and (forest[adjX][adjY] >= 1) and ((adjX,adjY) not in seen):
                        # if (nextX,nextY) == (0,0):
                        #     #print("seen for reaching {},{}: {}".format(nextX,nextY,seen))
                        #     print("queue: {}".format(queue))
                        queue.append((adjX,adjY,steps+1))
                        seen.add((adjX,adjY))
                #print("seen: {}".format(seen))

            #no such path exists
            return -1
        
        #start from 0,0 and have next be the first smallest tree, and use BFS for the others
        x,y = 0,0
        steps = 0
        #while there are still trees to cut
        while pq:
            _,nextX,nextY = heapq.heappop(pq)
            
            #find the shortest path to the next tree
            shortestPath = bfs(x,y,nextX,nextY)
            if shortestPath == -1:
                #print("forest: \n{}".format(np.array(forest)))
                return -1
            steps += shortestPath
            #print("total steps taken: {}".format(steps))
            x,y = nextX,nextY

        #print("forest at end: \n{}".format(np.array(forest)))
        return steps

def main():
    
    input = [[1,2,3],[0,0,4],[7,6,5]] #6
    input = [[1,2,3],[0,0,0],[7,6,5]] #-1
    input = [[2,3,4],[0,0,5],[8,7,6]] #6
    input = [[54581641,64080174,24346381,69107959],[86374198,61363882,68783324,79706116],[668150,92178815,89819108,94701471],[83920491,22724204,46281641,47531096],[89078499,18904913,25462145,60813308]] #57

    inputs = []
    
    testingOneInput = True
    if testingOneInput:
        #Test single input
        print("Input: \n{}".format(np.array(input)))

        solution = Solution()
        output = solution.cutOffTree(input)
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
#My previous submission on 05-31-2020 had TLE
class Solution(object):
    def cutOffTree(self, forest):
        
        # :type forest: List[List[int]]
        # :rtype: int
        

        curCoord = (0,0)
        totalDistance = 0
        
        ##create a dictionary to sort the height (low to high), mapping to coordinate
        # <height> --> list[<coordinate>]
        heightToCoordDict = {}
        for x,rowList in enumerate(forest):
            for y,height in enumerate(rowList):
                #if key is there, append to list, otherwise create new lists
                if height in heightToCoordDict.keys():
                    heightToCoordDict[height].append((x,y))
                else:
                    heightToCoordDict[height] = [(x,y)]

        #sort height in order of low to high
        ###print("heightToCoordDict before: ", heightToCoordDict)
        dictionary_items = heightToCoordDict.items()
        sortedHeightToCoordList = sorted(dictionary_items)
        ###print("sorted list: ", sortedHeightToCoordList)
                
        #iterate through each target coord in order of lowest height
        #sortedHeights = sorted(heightToCoordDict.keys(), reverse=True) #reverse order (ignore this)
        ####print("Printing height in heightToCoordDict")
        for item in sortedHeightToCoordList:
            height = item[0]
            ####print(height)
            if(height>1):
                #for trees>1, cut tree

                coordList = item[1]
                for coord in coordList:

                    #use BFS to find the shortest path to the next heighest tree
                    shortestDist = self.BFS(curCoord,coord,forest)
                    ####print("shortest dist: {0}".format(shortestDist))
                    if(shortestDist == -1):
                        #if coordinate is not reachable then we're done
                        return -1

                    #update distance
                    totalDistance += shortestDist
                    ###print("totalDistance: {0}".format(totalDistance))
                    
                    #change curCoord to coord(to)
                    curCoord = coord

        return totalDistance
    
    #BFS returns the shortest distance from coord(at) to coord(to)
    def BFS(self,at,to,forest):
        
        depth = 0
        queue = [] #stores the nodes we still need to visit (which will append its children to the end of the queue)
        visited = [] #stores the coordinates that were visited

        #if the starting point is already at the goal coord then return 0
        if(at == to):
            return depth
        
        #append coord node to queue and iterate through the queue as long as there are children
        node = (at,depth) #node is a pair with pair[0]=coord, pair[1]=depth
        queue.append(node)
        while(queue):
            ###print("--------------------------------------------------------------------")
            ###print("prev_at: {0}, goal: {1}".format(at,to))
            ###print("queue: {0}".format(queue))
            ###print("visited: {0}".format(visited))
            at = queue[0][0]
            depth = queue[0][1]
            
            #check if those coords are valid (i.e. >=0, not yet visited, not height 0) and then add to queue
            if(at[0]<0 or at[1]<0 or at[0]>=len(forest) or at[1]>=len(forest[0])):
                #not in the coordinate space, skip node
                queue.pop(0)
            elif(forest[at[0]][at[1]]==0):
                #height 0, can't go here
                queue.pop(0)
            elif(at in visited):
                #already visited, skip node
                queue.pop(0)
            else:
                #if at destination then return shorestDist
                if(at == to):
                    ###print("Reached to: {0}".format(to))
                    return depth
                
                childDepth = depth + 1

                ###print("at before tuple addition: {0}".format(at))
                #otherwise append children and keep visiting
                east = (tuple(map(lambda x, y: x + y, at, (0,1))), childDepth) #tuple addition at + (0,1)
                west = (tuple(map(lambda x, y: x + y, at, (0,-1))), childDepth)
                north = (tuple(map(lambda x, y: x + y, at, (1,0))), childDepth)
                south = (tuple(map(lambda x, y: x + y, at, (-1,0))), childDepth)
                queue.append(north)
                queue.append(south)
                queue.append(east)
                queue.append(west)
                ###print("queue after append NSEW: {0}".format(queue))

                #add current node to visit4ed
                visited.append(at)

                #done with this node, pop it
                queue.pop(0)

            
            ###print("--------------------------------------------------------------------")
            
        #visited all nodes, but no path to coord(to); return -1
        return -1
"""