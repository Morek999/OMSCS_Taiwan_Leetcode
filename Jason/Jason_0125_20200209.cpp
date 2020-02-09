/*
   The method I come up is really simple. Just define two pointers, one starts from the beginning of the string and the other starts from 
   the end of the string. Then we move the pointers to find the alphabetic character, and convert those two characters to lower case and compare.
   If they are equal, then continue to compare the next one, if not just return false.

   Time complexity: O(n) since we need to go through the entire string
   Space complexity: O(1) since we only need two pointers.

*/
class Solution {
public:
    bool isPalindrome(string s) {
        if(s.size() == 0){
            return true;
        }
        int l = 0, r = s.size()-1;
        while(l<r){
            while(l<r && !isalnum(s[l])){
                l++;
            }
            while(l<r && !isalnum(s[r])){
                r--;
            }
            if(tolower(s[l]) != tolower(s[r])){
                return false;
            }
            l++;
            r--;
        }
        return true;
    }
};