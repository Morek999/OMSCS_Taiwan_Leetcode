class Solution {
    public int numJewelsInStones(String J, String S) {
        
        int out = 0;
        for (int i = 0; i < S.length(); i ++) {
            if (J.indexOf(S.charAt(i)) >= 0) out += 1;
        }
        return out;
    }
}
