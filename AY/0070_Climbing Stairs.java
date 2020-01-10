class Solution {
    public int climbStairs(int n) {
        if (n == 0) return 1;
        // Same as the Approach 5: DP in solution
        List<Integer> res = new ArrayList<Integer> ();
        for (int i = 0; i < n; i ++) {
            if (i == 0) res.add(1);
            else if (i == 1) res.add(2);
            else res.add(res.get(i-1) + res.get(i-2));
            
        }
        
        return res.get(res.size() - 1);
    }
}


// Time: O(n)
// Space: O(n)
