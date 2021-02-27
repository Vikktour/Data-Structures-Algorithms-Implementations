"""
Victor Zheng
02-27-2021
29. Divide Two Integers (Medium)
""" 
"""
Approach1: 
O(log^2(N)) runtime where N = dividend (takes logN time to find the next closest term <= divisorRemaining, and we iterate logN times because we iterate until divisorRemaining is 0) - 28ms (92.03%)
O(1) space - 14.4MB (0%)
Bit manipulation with divisor doubling (to get to dividend in log time).

Let's say Q = dividend // divisor
We can factorize dividend in the form of dividend = a1divisor*2^n + a2*divisor*2^(n-1) + ... + a_(n-1)*divisor*2^1 + a_n*divisor*2^0 + r
Note that r is the remainder that isn't divisible by divisor. a1,a2,...,a_n are coefficients that are either 0 or 1.

Example: Let's say dividend=125 and divisor=3
Here are the terms of 3*2^i: 3,6,12,24,48,96
Then we can factorize dividend to be 125 = 96 + 24 + 3 + 2 = 3*2^5 + 3*2^3 + 3*2^0 + 2.
To get the solution, we ignore the remainder (remember we want to truncate the answer), and divide the entire expression by 3, which in this case is
to done by simply factoring the "3" coefficient, and taking the sum of the other components. So our answer is 2^5+2^3+2^0 = 32+8+1=41.

In our code, we do not have to factorize the dividend, we just need to find the next highest divisor*2^i that is <= what remains of dividend, and add the 2^i to our result.

idea adapated from: https://leetcode.com/problems/divide-two-integers/discuss/13407/C%2B%2B-bit-manipulations
I also improved the solution to ensure that registers only hold values in range [−2^31,  2^31 − 1].
"""
"""
#This solution breaks the <= 2^31-1 rule. To fix this, we can set a limit to < 2*31/2 in order to bit shift left (this is only for +). For -, we don't need it.
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
            
        #account for Q = 2^31 = -2^31/-1 case (because 2^31 doesn't fit in environment register range)
        if dividend == -2147483648 and divisor == -1:
            return 2147483647
        
        #first find the signs of the quotient
        if (dividend >= 0 and divisor >= 0) or (dividend <= 0 and divisor <= 0):
            sign = 1
        else:
            sign = -1

        #force both integers to positive to make the following operations easier. We will add the sign at the end.
        dividend = abs(dividend)
        divisor = abs(divisor)
        
        result = 0 #cumulative sum of 2*i
        remaining = dividend #how much of dividend is left that we still need to break into terms
        
        #keep iterating until we found all terms
        while remaining >= divisor:
            termVal = divisor #keeps track of value of divisor*2^i
            amount = 1 #keeps track of what "2^i" is in divisor*2^i
            while remaining >= termVal:
                #keep multiplying tempVal by 2 (using bit-shift) until we reach a value closest but <= remaining
                termVal <<= 1 #be careful here though, because termVal might go to 2^31, which is not allowed. - comeback1
                amount <<= 1

            # we past the goal, shift back and update variables
            termVal >>= 1
            amount >>= 1
            result += amount
            remaining -= termVal
            #print("amount={},result={},remaining={}".format(amount,result,remaining))
        
        #adjust result to have the sign we intend the quotient to be
        if sign == -1: result = -result
        return result
"""
#account for "Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−2^31,  2^31 − 1]."
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
            
        #account for Q = 2^31 = -2^31/-1 case (because 2^31 doesn't fit in environment register range)
        if dividend == -2147483648 and divisor == -1:
            return 2147483647
        
        #first find the signs of the quotient
        if (dividend >= 0 and divisor >= 0) or (dividend <= 0 and divisor <= 0):
            sign = 1
        else:
            sign = -1

        #force both integers to positive to make the following operations easier. We will add the sign at the end.
        extraRemainder = 0
        if dividend == -2147483648:
            dividendNew = 2147483647
            extraRemainder = 1 #need to account for this at the end to see if we need to +1 to our result due to this hovering 1
        else:
            dividendNew = abs(dividend)
        
        if divisor == -2147483648:
            if dividend == -2147483648:
                return 1
            else:
                return 0
        else:
            divisorNew = abs(divisor)
        
        result = 0 #cumulative sum of 2*i
        remaining = dividendNew #how much of dividend is left that we still need to break into terms
        
        #keep iterating until we found all terms
        while remaining >= divisorNew:
            termVal = divisorNew #keeps track of value of divisor*2^i
            amount = 1 #keeps track of what "2^i" is in divisor*2^i
            while remaining >= termVal:
                if termVal >= 1073741824 or remaining < (termVal << 1): # make sure we don't double 2147483648/2
                    break
                else:
                    #keep multiplying tempVal by 2 (using bit-shift) until we reach a value closest but <= remaining
                    termVal <<= 1 #be careful here though, because termVal might go to 2^31, which is not allowed. - comeback1
                    amount <<= 1

            result += amount
            remaining -= termVal
            #print("amount={},result={},remaining={}".format(amount,result,remaining))
        
        if extraRemainder == 1:
            #our dividend was -2^31, so account for the extra 1 to see if it mattered
            if remaining + extraRemainder == abs(divisor): #note that divisor here cannot be -2^31 because we had a return statement at the top for this case
                result += 1

        #adjust result to have the sign we intend the quotient to be
        if sign == -1: result = -result
        return result

"""
Approach2: O(log^2(N)) runtime where N is dividend. O(1) space.
Bitwise Long division.
Convert integer into bit notation and then do long division. Note that It's using solely addition and subtraction since we don't have to multiply.
https://www.youtube.com/watch?v=hygRTweKAOk&ab_channel=ProgrammingLivewithLarry  
"""

def main():
    """
    10
    3
    7
    -3
    0
    1
    1
    1
    125
    3
    -2147483648
    -1
    2147483647
    1
    -2147483648
    1
    """
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