
/*
My first version solution but only passed like half of the tesing case, but I am too busy to finish this question so I need to peek the answer QQ

class Solution {
public:
    int minMeetingRooms(vector<vector<int>>& intervals) {
        if(intervals.empty()){
             return 0;
        }
        vector<int> record(intervals.size(),0);
        int num = 1;
        for(int i = 0; i < intervals.size();i++){
            for(int j = i+1; j < intervals.size();j++){
                if(covered(intervals[i],intervals[j])&&(!record[i] || !record[j])){
                    num++;
                    record[i] = 1;
                    record[j] = 1;
                    break;
                }
            }
        }
        return num;
    }
private:
    bool covered(vector<int>& a, vector<int>& b){
        int minvalue = max(a[0],b[0]);
        int maxvalue = min(a[1],b[1]);
        return minvalue < maxvalue;
    }
};
*/