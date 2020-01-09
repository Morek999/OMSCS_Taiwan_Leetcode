class Solution {
public:
    bool canAttendMeetings(vector<vector<int>>& intervals) {
        if(intervals.empty()){
             return true;
        }
        for(int i = 0; i < intervals.size();i++){
            for(int j = i+1; j < intervals.size();j++){
                if(covered(intervals[i],intervals[j])){
                    return false;
                }
            }
        }
        return true;
    }
private:
    bool covered(vector<int>& a, vector<int>& b){
        int minvalue = max(a[0],b[0]);
        int maxvalue = min(a[1],b[1]);
        return minvalue < maxvalue;
    }
};