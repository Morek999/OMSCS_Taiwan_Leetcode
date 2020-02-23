/*
Thought: use hash map to count for the frequencies for each element. And then use max heap (size = K) to get the top K freqeuent elements
Time complexity: build the hash map is O(n), and build the max heap with size K is nlogk (if it's just insert on average it's O(1), but worst could
be O(logk), and if size > k you need to pop one element, and pop is O(logk) -- https://stackoverflow.com/questions/52556930/time-complexity-of-the-heap-pop-operation
So here build the max heap with size k the time complexity is O(nlogk))
and eventually just pop out all of the elements in the heap and put in the answer vector(klogk), then reverse the answer vector(O(n))
--- > the time complexity for this problem is O(nlogk)
Space complexity: O(k)
Suggested problem: LC 692 Top K Frequent Words: https://leetcode.com/problems/top-k-frequent-words/
*/
class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int,int> m;
        for(int num:nums){
            m[num]++;
        }
        
        auto comp = [](const pair<int,int>& a, pair<int,int>& b){
            return a.second > b.second;
        };
        
        priority_queue<pair<int,int>, vector<pair<int,int>>, decltype(comp)> q(comp);
        
        for(const auto& kv: m){
            q.push(kv);
            if(q.size() > k) q.pop();
        }
        
        vector<int> ans;
        
        while(!q.empty()){
            ans.push_back(q.top().first);
            q.pop();
        }
        reverse(ans.begin(),ans.end());
        return ans;

    }
};