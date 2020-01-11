class Solution {
public:
    int numJewelsInStones(string J, string S) {
        if(S.empty() || J.empty()){
            return 0;
        }
        unordered_set<char> j;
        for(char c:J){
            j.insert(c);
        }
        int ans = 0;
        for(char s:S){
            if(j.find(s) != j.end()){
                ans++;
            }
        }
        return ans;
    }
};