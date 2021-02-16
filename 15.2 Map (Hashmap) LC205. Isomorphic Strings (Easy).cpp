/*
Victor Zheng
02-01-2021
205. Isomorphic Strings (Easy)
*/

#include <iostream>
#include <string>
#include <vector>
#include <algorithm> //sort
#include <set> //set and multiset - sorted containers (min to max) - similar to heap in python
#include <map>
using namespace std;

/*
Approach: O(n) runtime, O(1) space - 8ms(70.63%),7MB(77.74%)
Iterate s and t at the same time, and map s[index] to t[index].

Can't do
1) o->a and o->r
2) b->b and d->b
*/
class Solution {
public:
    bool isIsomorphic(string s, string t) {
        map<char, char> s_to_t;
        map<char, char> t_to_s;
        int sz = s.length();
        for (int index = 0; index < sz; index++) {
            char sLetter = s[index];
            char tLetter = t[index];
            if (s_to_t.count(sLetter) > 0) {
                //key exists, check if mapping is still to same char (o->a and o->r case)
                if (s_to_t[sLetter] != tLetter)
                    //mapping not the same and we can't change it, so return false
                    return false;
            }
            else {
                //create a mapping
                s_to_t[sLetter] = tLetter;
            }
            //check for b->b and d->b case
            if (t_to_s.count(tLetter) > 0) {
                if (t_to_s[tLetter] != sLetter)
                    return false;
            }
            else {
                t_to_s[tLetter] = sLetter;
            }
        }
        return true;
    }
};



int main()
{
	//auto s = "egg", t = "add"; //true
	//auto s = "bbbaaaba", t = "aaabbbba"; //false
	auto s = "aabc", t = "xyyz"; //false
	//cout << "input: " << input << endl;
	//printf("input: s=%s, t=%s", s, t);
	//for printing vectors
	/*
	cout << "[";
	for (auto& val : input) {
		cout << val;
		if (&val != &input.back()) printf(", ");
	}
	cout << "]\n";
	*/

	Solution solution = Solution();
	auto output = solution.isIsomorphic(s,t);
	cout << "output: " << output << endl;

}

/*
Approach: FAIL - I needed to also account for position (e.g. s="ab" t="aa" is false because a->a, and b->a is not allowed due to mapping to same char).
Get the frequencies for both s and t. See if they have the same of each frequncy.

*/
/*
class Solution {
public:
    bool isIsomorphic(string s, string t) {
        //get a frequency list for each letter - map it and then insert into list
        map<char, int> freqS;
        map<char, int> freqT;
        for (char c : s) {
            if (freqS.count(c) > 0)
                freqS[c] += 1;
            else
                freqS[c] = 1;
        }
        for (char c : t) {
            if (freqT.count(c) > 0)
                freqT[c] += 1;
            else
                freqT[c] = 1;
        }
        //put values of each into multiset and check if they are equal
        multiset<int> setS;
        multiset<int> setT;
        for (auto const& [key, val] : freqS) {
            setS.insert(val);
        }
        for (auto const& [key, val] : freqT) {
            setT.insert(val);
        }

        //prints for debugging
        //cout << "setS: ";
        //for (int const& val : setS) {
        //    cout << val << " ";
        //}
        //cout << endl;
        //cout << "setT: ";
        //for (int const& val : setT) {
        //    cout << val << " ";
        //}
        //cout << endl;

        return setS == setT;
    }
};
*/