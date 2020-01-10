class Solution {
    public int minMeetingRooms(int[][] intervals) {
        
        
        // the idea is the same as 0252 but use map to store the num of room
        Map<Integer, Integer> occupied = new HashMap<Integer, Integer>();
        int room = 0;
        
        for (int i = 0; i < intervals.length; i ++) {
            int startTime = intervals[i][0];
            int endTime = intervals[i][1];
            
            for (int t = startTime + 1; t <= endTime; t ++) {
                if (!occupied.containsKey(t)) occupied.put(t, 1);
                else occupied.put(t, occupied.get(t) + 1);
                if ( occupied.get(t) > room ) room = occupied.get(t);
            }
        }
        return room;   
    }
}

// This method is almost brute force. XD 
// can only pass simple short input... 
// Time: O(n*k) 
// Space: O(n*k)
