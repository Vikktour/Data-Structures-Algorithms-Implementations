/*
Victor Zheng
01-29-2021
279. Perfect Squares (Medium)
*/

#include <iostream>
#include <string>
#include <vector>
#include <algorithm> //sort
using namespace std;

/*
Approach: O(n*numSquaresLessThanN) < O(n*sqrt(n)) runtime, O(n) space - 68ms(85%), 9.1MB (64%)
Dynamic programming, where each dp[i] only needs to look for the prev square numbers.
*/

class Solution{
public:
	int numSquares(int n) {
		//int dp[n] = { 0 }; //can't do this bc n is not constant.
		vector<int> dp(n + 1, INT_MAX); //n+1 entries of INT_MAX
		dp[0] = 0;

		//i is our current index in dp
		for (int i = 1; i <= n; i++) {
			//perfect squares only need 1 step
			if (floor(sqrt(i)) * floor(sqrt(i)) == i) {
				dp[i] = 1;
				continue;
			}

			//j is our stepback
			int minSteps = INT_MAX; //get the best j stepback
			for (int j = 1; j*j < i; j++){
				int steps = dp[i - j*j];
				//printf("dp[%d]=%d\n", i - j * j, steps);
				if (steps < minSteps) {
					minSteps = steps;
					//printf("j^2=%d, steps=%d, minSteps=%d\n", j * j, steps, minSteps);	
				}
			}
			//printf("index %d, minSteps %d\n", i, minSteps);
			dp[i] = 1 + minSteps;
		}

		//cout << "dp: ";
		//int index = 0;
		//for (auto val : dp) {
		//	cout << index++ << " ";
		//}
		//cout << endl;
		//
		//cout << "dp: ";
		//for (auto val:dp) {
		//	cout << val << " ";
		//}
		//cout << endl;
		return dp[n];
	}
};

int main()
{
	auto input = 12;
	cout << "input: " << input << endl;

	Solution solution = Solution();
	auto output = solution.numSquares(input);
	cout << "output: " << output << endl;

}
