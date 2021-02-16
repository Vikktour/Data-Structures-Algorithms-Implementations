"""
Victor Zheng
02-14-2021
785. Is Graph Bipartite? (Medium)
""" 
"""
Approach: O(V+E) runtime for BFS, O(V) space for colors - 172ms (78.97%), 14.5 (97.66%)
Label each vertex a color (white=unvisited=0, blue=leftside=1, red=rightside=2)
Use BFS to assign colors and return False if we try to color an adjacent node with an opposite color (i.e. blue-->red, or red-->blue)

Idea from Larry: https://www.youtube.com/watch?v=KzLjSb00HOM&ab_channel=ProgrammingLivewithLarry
"""
from typing import List 
import collections
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        
        N = len(graph)
        white, blue, red = 0,1,2
        colors = [white] * N #each index in colors represent a vertex; their colors are initialized as white (unvisited)
        
        #BFS - starting from startNode, color all other connected vertices
        #startNode is in format of [vertex,color]
        def bfsColor(startNode):
            queue = collections.deque()
            queue.append(startNode)
            
            while queue:
                vertex, color = queue.popleft()
                oppositeColor = red if color == blue else blue
                #check all vertices adjacent to this vertex and color any uncolored ones to the opposite color
                for adjVertex in graph[vertex]:
                    if colors[adjVertex] == white:
                        #set color to opposite color
                        colors[adjVertex] = oppositeColor
                        queue.append((adjVertex,colors[adjVertex]))
                    #adjVertex not white, check if it's opposite color otherwise false
                    elif colors[adjVertex] != oppositeColor:
                        return False
                    #print("colors: {}".format(colors))
            return True
        
        #note that we use for loop here in case there are multiple graphs that are disconnected. We need to make sure all graphs are bipartite.
        for vertex in range(N):
            color = colors[vertex]
            if color == white:
                #if not visited yet, visit the vertex
                color = colors[vertex] = blue #i'll abitrarily set the first color to blue
                startNode = (vertex, color)
                if not bfsColor(startNode):
                    return False
        return True

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