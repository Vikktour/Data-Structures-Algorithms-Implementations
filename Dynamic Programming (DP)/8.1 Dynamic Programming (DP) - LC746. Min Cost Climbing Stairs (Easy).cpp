/*
Victor Zheng
01-30-2021
746. Min Cost Climbing Stairs (Easy)
*/

#include <iostream>
#include <string>
#include <vector>
#include <algorithm> //sort
#include <set> //set and multiset - sorted containers (min to max) - similar to heap in python
using namespace std;

/*
Approach1: O(2^n) runtime - TLE, O(n) memory for recursive stack.
Recursion - brute force - start from end and recursively have it depend on the min of previous 2 values.

Awesome guide for full DP progression - https://leetcode.com/problems/min-cost-climbing-stairs/discuss/476388/4-ways-or-Step-by-step-from-Recursion-greater-top-down-DP-greater-bottom-up-DP-greater-fine-tuning
*/
/*
class Solution {
public:
	int minCostClimbingStairs(vector<int>& cost) {
		cost.push_back(0); //for the case where we take 2 steps from second to last element
		return minCost(cost.size() - 1, cost);
	}

	int minCost(int index, vector<int>& cost) {
		if (index == 0)
			return cost[0];
		else if (index == 1)
			return cost[1];

		return cost[index] + min(minCost(index - 1, cost), minCost(index - 2, cost));
	}
};*/

/*
Approach2: O(n) runtime, O(n) memory - 12ms, 13.8MB
Top-down DP - Using memoization along with approach1.
*/
/*
class Solution {
public:
	vector<int> dp;
	int minCostClimbingStairs(vector<int>& cost) {
		cost.push_back(0); //for the case where we take 2 steps from second to last element
		int size = cost.size();
		dp.resize(size, -1);
		dp[0] = cost[0], dp[1] = cost[1];
		return minCost(size - 1, cost);
	}

	int minCost(int index, vector<int>& cost) {

		if (dp[index] != -1)
			return dp[index];

		int result = cost[index] + min(minCost(index - 1, cost), minCost(index - 2, cost));
		dp[index] = result;
		return result;
	}
};*/

/*
Approach3: O(n) runtime, O(n) space - 4ms(96.47%),13.7MB(76.48%)
Bottom-up DP - getting rid of recursion and just use array indexing
*/
/*
class Solution {
public:
	vector<int> dp;
	int minCostClimbingStairs(vector<int>& cost) {
		cost.push_back(0); //for the case where we take 2 steps from second to last element
		int size = cost.size();
		dp.resize(size, -1);
		dp[0] = cost[0], dp[1] = cost[1];
		for (int index = 2; index < size; index++) {
			dp[index] = cost[index] + min(dp[index - 1], dp[index - 2]);
		}
		return dp[size - 1];
	}
};
*/

/*
Approach4: O(n) runtime, O(1) space - 4ms (96.47%), 13.6MB (85.16%)
Fine Tuning - Drop the dp array, and keep reference of previous 2 indices
*/
class Solution {
public:
	int minCostClimbingStairs(vector<int>& cost) {
		cost.push_back(0); //for the case where we take 2 steps from second to last element
		int size = cost.size();
		int left1 = cost[0], left2 = cost[1];
		int right = INT_MAX;
		for (int index = 2; index < size; index++) {
			right = cost[index] + min(left1, left2);
			left1 = left2;
			left2 = right;
		}
		return right;
	}
};

int main()
{
	//vector<int> input = {10, 15, 20}; //15
	vector<int> input = { 1, 100, 1, 1, 1, 100, 1, 1, 100, 1 }; //6
	//cout << "input: " << input << endl;

	Solution solution = Solution();
	auto output = solution.minCostClimbingStairs(input);
	cout << "output: " << output << endl;

}
