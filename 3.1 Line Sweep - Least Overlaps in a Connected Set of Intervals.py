"""
Victor Zheng
02-04-2021
1. Least Overlaps in a Connected Set of Intervals
Question: Given a set of intervals where each interval overlaps at least 1 other interval, 
find the least overlapping interval within bounds of the original set.
Note that this output interval doesn't have to be the same as one of the input intervals.
Ex1: 
input = [[0,3],[3,7],[0,3],[5,8]]
output - [4,5]

Challenge: There can be multiple intervals that is least overlapping, but can you provide the longest?
""" 
"""
Approach1:
Line sweep
Create an event list that holds (pos,event) where pos is the position on the numberline and event represents open or close bracket of the interval (I'll use "open" and "close" to represent the event)
Sort event list by increasing pos. This lets us traverse the events sequentiallly.

Have a variable "enclosed" that keeps track of the number of intervals we're currently inside. Also have two variables "startX" and "endX" to keep track of the minimum overlapping interval.
Now iterate through the events, and for each time there's an open event, we +1 to enclosed, and for each time there's a close event, we -1 to enclose.
Whenever there is a new minimum number of enclosed, we reset startX to current position, and keep iterating until the number of enclosed go back up, that's when we save the endX position.
To get the longest interval, we can dedicate another 2 set of variables "startXL" "endXL" to store the current maximum length - minimum overlapping interval. 
Upon seeing new "startX" and "endX" we do endX-startX and comapre with endXL-startXL to see which is bigger, and take the bigger one to be the new "startXL" and "minXL"
"""
from typing import List
"""
#Might have some bugs since I updated it in my next solution
class Solution:
    def minOverlap(self, intervals:List[int]) -> List[int]:
        
        #create event list holding (pos,event)
        events = []
        for interval in intervals:
            events.append((interval[0],"open"))
            events.append((interval[1],"close"))
        events.sort(reverse=True) #sort by decreasing pos (since we will be popping right to retrive position)
        
        smallestEnclosed = float("inf")
        prevEnclosed = 0 #for checking if we modify endX to see new result interval
        enclosed = 0 #number of intervals we're currently inside
        startX, endX = 0, 0 #current valid result interval
        startXL, endXL = 0, 0 #current largest valid result interval

        while events:
            #update all events that are on the same position
            newPos = events[-1][0]
            prevEnclosed = enclosed
            while events and events[-1][0] == newPos:
                event = events.pop()
                if event[1] == "open":
                    enclosed += 1
                else:
                    enclosed -= 1
            if enclosed == 0:
                #reached the end of intervals, so we need to force it to prevSmallest (to say that there are no smaller number of overlaps than 1) so the following lines can execute properly
                enclosed = smallestEnclosed
            #check if there's new smallest enclosed
            if enclosed < smallestEnclosed:
                #new smallest number of overlapping intervals, so start new result interval
                startX = newPos
                smallestEnclosed = enclosed
                startXL, endXL = 0, 0 #for resetting interval size
            elif enclosed == smallestEnclosed:
                #keep scanning for endX
                pass
            else: #enclosed > smallestEnclosed
                #check if prev enclosed was smallest, and then update endX
                if prevEnclosed == smallestEnclosed:
                    endX = newPos
                    #check if this new interval is biggest
                    intervalSize = endX - startX
                    if intervalSize > endXL - startXL:
                        #it is indeed largest interval of minimum overlaps, so update it
                        startXL = startX
                        endXL = endX 
        #check one last time for very last pos to see if there's update
        #check if prev enclosed was smallest, and then update endX
        if prevEnclosed == smallestEnclosed:
            endX = newPos
            #check if this new interval is biggest
            intervalSize = endX - startX
            if intervalSize > endXL - startXL:
                #it is indeed largest interval of minimum overlaps, so update it
                startXL = startX
                endXL = endX
        return [startXL,endXL]
"""
"""
#Adaptation: 
accept the opens first, then calculate enclosed, then use that as enclosedPos for number of enclosed prior to the close disapppearing, 
then based on opens, we set endX -1 to the left if enclosedPos is too big.
We also set startX at +1 of pos if the pos has a big enclosedPos.

The previous attempt assumed that each interval does not include the close part i.e. [a,b) was assumed instead of [a,b].
To account for that, we can use enclosedDuring and enclosedAfter variables. enclosedDuring includes closing brackets in the enclosed.
enclosedAfter is when we subtract away the closingBrackets from enclosed.

Still has minor bugs but the previous solution (above) seems more correct now that I think about it, based on problem. Because the interval should 
ignore the number of enclosed at point value anyways if we look at it area-wise.

The question I'm solving assumes that points of overlap do matter, not just area. And we can have output length be as small as 0 (if it is a minimum overlap) - Ex: input = [[0,3],[3,7],[0,3],[5,8]] #[4,4]
"""

class Solution:
    def minOverlap(self, intervals:List[int]) -> List[int]:
        
        #create event list holding (pos,event)
        events = []
        for interval in intervals:
            events.append((interval[0],"open"))
            events.append((interval[1],"close"))
        events.sort(reverse=True) #sort by decreasing pos (since we will be popping right to retrive position)
        
        smallestEnclosed = float("inf") #smallest valid number of enclosed intervals so far
        prevEnclosed = 0 #for checking if we modify endX to see new result interval
        enclosedDuring, enclosedAfter = 0, 0 #number of intervals we're currently inside
        startX, endX = 0, 0 #current valid result interval
        startXL, endXL = 0, -1 #current largest valid result interval #initialize -1 intervalSize, so it will update for the case where we have size 0 but new minimum low

        while events:
            #update all events that are on the same position
            newPos = events[-1][0]
            print("checking position: {}".format(newPos))
            print(startXL,endXL)
            prevEnclosed = enclosedAfter
            newOpen, newClosed = 0, 0 #keeps track of number of open and closed brackets for this pos
            while events and events[-1][0] == newPos:
                event = events.pop()
                if event[1] == "open":
                    newOpen += 1
                else:
                    newClosed += 1
            enclosedDuring = prevEnclosed + newOpen
            enclosedAfter = enclosedDuring - newClosed
            print("enclosedDuring={},enclosedAfter={}".format(enclosedDuring,enclosedAfter))
            if enclosedAfter == 0:
                #reached the end of intervals, so we need to force it to 1 (to say that there are no smaller number of overlaps than 1) so the following lines can execute properly
                enclosedAfter = smallestEnclosed
            #check if there's new (or same) smallest enclosed
            if enclosedAfter < smallestEnclosed:
                #new smallest number of overlapping intervals, so start new result interval
                if enclosedDuring == enclosedAfter:
                    startX = newPos
                else:
                    startX = newPos + 1 #note we do +1 so we don't include the pos with brackets that are exiting
                smallestEnclosed = enclosedAfter
                startXL, endXL = 0, -1 #for resetting interval size
            elif enclosedAfter == smallestEnclosed:
                #check if it's another set of interval that has same minOverlap, but we closed previous, so we would be starting a new one now
                if enclosedAfter != prevEnclosed:
                    if enclosedDuring == enclosedAfter:
                        startX = newPos
                    else:
                        startX = newPos + 1 #note we do +1 so we don't include the pos with brackets that are exiting
                else:
                    pass
            else: #enclosedAfter > smallestEnclosed
                #check if prev enclosed was smallest, and then update endX
                if prevEnclosed == smallestEnclosed:
                    if prevEnclosed == enclosedDuring:
                        endX = newPos
                    else: #prevEnclosed < enclosedDuring
                        #new enclosing is too big due to added open intervals, so take pos-1
                        endX = newPos - 1
                    #check if this new interval is biggest
                    intervalSize = endX - startX
                    if intervalSize > endXL - startXL:
                        #it is indeed largest interval of minimum overlaps, so update it
                        startXL = startX
                        endXL = endX 
        #check one last time for very last pos to see if there's update
        #check if prev enclosed was smallest, and then update endX
        if prevEnclosed == smallestEnclosed:
            if prevEnclosed == enclosedDuring:
                endX = newPos
            else: #prevEnclosed < enclosedDuring
                #new enclosing is too big due to added open intervals, so take pos-1
                endX = newPos - 1
            #check if this new interval is biggest
            intervalSize = endX - startX
            if intervalSize > endXL - startXL:
                #it is indeed largest interval of minimum overlaps, so update it
                startXL = startX
                endXL = endX 
        return [startXL,endXL]

def main():

    input = [[0,3],[0,3]] #[0,3]
    #input = [[0,4],[2,3]] #[0,1]
    input = [[1,5],[3,6],[6,7]] #[1,2]
    input = [[0,3],[3,7],[0,3],[5,8]] #[4,4]

    # BAD TEST CASE input = [[0,3],[3,7],[0,3],[5,8]] #[4,5]

    inputs = []
    
    testingOneInput = True
    if testingOneInput:
        #Test single input
        print("Input: {}".format(input))

        solution = Solution()
        output = solution.minOverlap(input)
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