/*
Victor Zheng
01-31-2021
19. Remove Nth Node From End of List (Easy)
*/

#include <iostream>
#include <string>
#include <vector>
#include <algorithm> //sort
#include <set> //set and multiset - sorted containers (min to max) - similar to heap in python
using namespace std;


//Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};
 
 /*
 Approach: O(n) runtime, O(1) space - 8ms (35.27%), 10.7MB (70.9%)
 2 pointer sliding window - left and right = left + n.
 Upon current reaching left+n-1, we want to start moving left and right pointers forward on each iteration.
 Upon reaching the last element, we remove left->next
 */
class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode* left = head;
        ListNode* right = head;
        //get the right pointer which is left + n - 1
        for (int i = 0; i < n; i++) {
            right = right->next;
        }

        if (right == nullptr) {
            //first element needs to be deleted
            ListNode* deletedNode = head;
            head = head->next;
            delete deletedNode;
            return head;
        }

        while (right->next != nullptr) {
            //keep shifting left and right pointer forward until we reached the end
            left = left->next;
            right = right->next;
        }
        //now that we're at the end, remove left->next
        ListNode* deletedNode = left->next;
        left->next = left->next->next;
        delete deletedNode;
        return head;
    }
};

int main()
{
	auto input = "";
	cout << "input: " << input << endl;
	//printf("input: s=%s, t=%s", s, t);
	//for printing vectors
	/*
	cout << "[";
	for (auto& val : input) {
		cout << val;
		if (&val != &input.back()) printf(", ");
	}
	cout << "]\n";*/

	Solution solution = Solution();
	auto output = solution.func(input);
	cout << "output: " << output << endl;

}
