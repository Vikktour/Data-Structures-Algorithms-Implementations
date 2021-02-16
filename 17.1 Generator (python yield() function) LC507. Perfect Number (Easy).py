"""
Victor Zheng
02-10-2021
507. Perfect Number (Easy)
""" 
"""
Approach1: TLE - O(n) runtime, O(1) space
Brute force up till ceil(n/2) check if divisor and add to divisorSum. Check if divisorSum == num at end.
"""
import math
"""
class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        
        divisorSum = 0
        for x in range(1,math.ceil(num/2)+1):
            if num%x==0:
                divisorSum += x
                #print("divisor: {}".format(x))
        #print(divisorSum,num)
        return (divisorSum == num)
"""

"""
Approach2: O(sqrt(N)) runtime, O(1) space generator (lazy evaluation) - not really a good interview approach since it's mathy - 40ms(66.82%),14.3MB(13.25%)
Prime Factorization - we keep dividing by smaller numbers so N.
Implementation by Alex Wice: https://leetcode.com/problems/perfect-number/discuss/98636/Python-Straightforward-with-Explanation
Generator - https://wiki.python.org/moin/Generators
"""
"""
class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        def prime_factorization(N):
            d = 2
            while d * d <= N:
                expo = 0
                while N % d == 0:
                    expo += 1
                    N /= d
                if expo:
                    yield (d, expo) #yields (d,expo) as pair in generator, and then keeps going in while loop to yield more pairs until we break out.
                d += 1
            if N > 1:
                yield (N, 1)

        #checking what the generator creates
        #for pair in prime_factorization(abs(num)):
        #    print("pair: {}".format(pair))

        ans = 1
        for prime, expo in prime_factorization(abs(num)):
            #each time these two linee are called, we multiple any with the sum of factors that are multiples of "prime" up till "expo" amount of terms
            primeMultipleSum = sum(prime ** k for k in range(expo + 1)) 
            ans *= primeMultipleSum 
            #why multiply? it's a math formula -  2^i 3^j 5^k... for i in [0,a], j in [0,b] etc. The sum of all of these is simply (2^0 + 2^1 + ... + 2^a) * (3^0 + 3^1 + ... + 3^b) * (5^0 + 5^1 + ... + 5^c) *

            #for k in range(expo+1):
            #    print("prime**k={}".format(prime**k))
            #print("primeMultipleSum: {}".format(primeMultipleSum))
            
            #print("ans: {}".format(ans))

        
        #print(ans,num)
        return ans == 2*num
"""

""" 
Approach3: O(sqrt(n)) runtime, O(1) space - 36ms(82.65%), 14.1MB (92.50%)
Iterate up to sqrt(n) and take any pairs that divide n.
Ex: n=28, then we have (2,14), (4,7) pairs, and along with 1, adds up to 28.
reference: https://leetcode.com/problems/perfect-number/discuss/98616/Simple-Python
My discussion post: https://leetcode.com/problems/perfect-number/discuss/1060006/python-simple-sqrt-iteration-solution-comments
"""
class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        divisorSum = 1
        if num <= 4: #base cases (4 is the largest number that doesn't enter the for loop)
            return False
        for x in range(2,math.ceil(math.sqrt(num))): #range will purposely skip the square number (if there is one), otherwise, we just take anything to the left of sqrt(num)
            if num % x == 0:
                #print("factor pair: ({},{})".format(x,num//x))
                #found divisor, add both pairs
                divisorSum += x + (num//x) #num/x is the other factor that multiple to num
        #check if there's a square number term
        if (x+1)**2 == num:
            #exactly a square number (we left it out from the for loop to avoid double adding, so add it in here)
            divisorSum += x
        #print("divisorSum: {}".format(divisorSum))
        return divisorSum == num
    
def main():
    
    input = 1 #false
    #input = 2 #false
    input = 3
    input = 4
    input = 5
    #input = 28 #true
    #input = 8128 #true
    #input = 33550336 #true

    expected = ""

    inputs = []
    
    testingOneInput = True
    if testingOneInput:
        #Test single input
        print("Input: {}".format(input))

        solution = Solution()
        output = solution.checkPerfectNumber(input)
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