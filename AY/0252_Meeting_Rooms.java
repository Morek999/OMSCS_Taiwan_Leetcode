class Solution {
    public boolean canAttendMeetings(int[][] intervals) {
        if (intervals.length <= 1) return true;
        
        // Use a set to store "all" the times that are already occupied. 
        Set<Integer> occupied = new HashSet<Integer>();
        
        for (int i = 0; i < intervals.length; i ++) {
            int startTime = intervals[i][0];
            int endTime = intervals[i][1];
            for (int t = startTime+1; t <= endTime; t ++) {
                if (!occupied.contains(t)) occupied.add(t);
                else return false;
            }  
        }
        return true;
    }
}
