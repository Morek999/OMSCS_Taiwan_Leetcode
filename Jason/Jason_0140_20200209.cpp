/*
For this question I used a hashset to quickly check if a word is in the dictionary and memorization to improve the recursion efficiency
Check the picture I uploaded in the folder for the idea of solving this question.

I am not sure the time and space complexity analysis here, check few solutions but not very sure...
Time complexity: O(n^3), the recursion tree will take o(n^2) and combine will take O(n)
Space complexity: O(n^3), The depth of the recursion tree can go up to n and each activation record can contains a string list of size n.

*/
class Solution {
public:
    vector<string> wordBreak(string s, vector<string>& wordDict) {
        unordered_set<string> dict(wordDict.begin(), wordDict.end());
        unordered_map<string,vector<string>> mem;
        return wordBreak(s, dict, mem);
    }
private:// catsand 
    // >> combine({"cats and", "cat sand"}, "dog");
    // {"cats and dog", "cat sand dog"}
    vector<string> combine(const vector<string>& prefixes, const string& word) {
        vector<string> results;
        for(const auto& prefix : prefixes)
            results.push_back(prefix + " " + word);
        return results;
    }
    
    const vector<string> wordBreak(string s, unordered_set<string>& dict, unordered_map<string,vector<string>>& mem) {
        // Already in memory, return directly
        if(mem.count(s)){
            return mem[s];  
        } 
        
        // Answer for s
        vector<string> ans;
        
        // s in dict, add it to the answer array
        if(dict.count(s)) {
            ans.push_back(s);
        }
        
        for(int j=1;j<s.length();++j) {
            // Check whether right part is a word
            const string right = s.substr(j); // from j to the end
            if (!dict.count(right)){
                continue; 
            } 
            
            // Get the ans for left part, and then combine with the right word
            const string left = s.substr(0, j);
            const vector<string> left_ans = combine(wordBreak(left, dict, mem), right);
            
            ans.insert(ans.end(), left_ans.begin(), left_ans.end());
        }
        
        // we update the memorization here since we need to find all the solution, instead of just find one
        mem[s].swap(ans);
        return mem[s];
    }
};