"""
Victor Zheng
12-20-2020
973. K Closest Points to Origin (Medium)
""" 
"""
Approach1 ~ O(NlogN): find distance for each point and store in array (distance,coords). Sort array by distance and return the first k lowest distance.
Approach2 ~ O(N+(N-K)*logk): find distance for each point, and append to max heap up to k values. Whenever the top value is > new value, replace top value with new value and 
"""

#approach1
from typing import List
"""
class Solution:
    #O(nlogn)
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        if len(points) == 0:
            return []
        #get distances
        distances = [] #stores tuple (distance,coord)
        for [x,y] in points:
            distances.append((x**2+y**2,[x,y])) #note that we only need to have relative distance, so sqrt is not necessary
        #sort distances and return first k
        distances.sort()
        retCoords = []
        for _, coord in distances:
            retCoords.append(coord)
            if len(retCoords) == K:
                return retCoords
"""

#approach2
import heapq
class Solution:
    #692ms ~ O(n + (n-k)*logk)
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        if len(points) == 0:
            return []
        #get distances
        distances = [] #stores tuple (distance,coord)
        heapq.heapify(distances)
        for [x,y] in points:
            #note that we only need to have relative distance, so sqrt is not necessary
            distance = (-1*(x**2+y**2),[x,y]) #since heapq is a minheap, I use *-1 to the distance to imitate a maxheap
            if len(distances) == K:
                #keep heap size K. At size K, we swap whenever we see a lower distance value compared to the heap's highest value.
                if -1*distance[0] < -1*distances[0][0]: #compare new item with heap's max
                    #insert new distance if it's smaller
                    heapq.heappushpop(distances,distance)
            else:
                heapq.heappush(distances,distance)
        
        retList = []
        for distance,coord in distances:
            retList.append(coord)
        return retList

def main():
    
    points,k = [[1,3],[-2,2]], 1 #[-2,2]
    points,k = [[3,3],[5,-1],[-2,4]], 2 #[[3,3],[-2,4]]

    inputs = []
    
    testingOneInput = True
    if testingOneInput:
        #Test single input
        print("Input: points={0}, k={1}".format(points,k))

        solution = Solution()
        output = solution.kClosest(points,k)
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