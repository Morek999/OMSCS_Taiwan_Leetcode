/*
First I came out the brutal force method by checking every single person if this he/she is the celebrity. A helper function isCelebrity
is written. Suppose we want to if check a person i is the celebrity, then we just need to check if in all of the ppl, this person i knows
anyone or someone doesn't know person i, then i is not a celebrity. If this loop is successfully finished, then this person is a celebrity.
This is O(n^2) method(assuming knows(a,b) is a O(1) method), since first loop need to check n ppl and isCelebrity need to do 2*(n-1), so 
the total is n(2n-2) which leads to O(n^2)

A more elegant way is to use a loop to find the celebrity candidate first, then only check if this candidate is a celebrity.
To find the celebrity candidate, simply use a for loop to check, check the animation for a better explanation.
Then use the isCelebrity to check if this candidate is actually a celebrity. 
Time complexity: O(n), since first we use a for loop to find the candidate and then isCelebrity takes 2(n-1), so the total will be
3n-2 --> O(n)
Space complexity: O(1), since we only use a variable

There's an even better opimal method using cache, but haven't implemented it yet
 */

// Forward declaration of the knows API.
bool knows(int a, int b); // return if a knows b

// better way to reduce the check case
class Solution {
public:
    int findCelebrity(int n) {
        int celebritycand = 0;
        for(int i = 0; i < n; i++){
            if(knows(celebritycand,i)){
                celebritycand = i;
            }
        }
        if(isCelebrity(n,celebritycand)){
            return celebritycand;
        }
        return -1;
    }
    
    bool isCelebrity(int n, int i){
        for(int j = 0; j < n; j++){
            if(j == i){ // don't ask if i knows i
                continue;
            }
            // if i person knows someone, or someone doesn't know i
            // then i is not a celebrity
            if(knows(i,j) || !knows(j,i)){ 
                return false;
            }
        }
        return true;
    }
};

// brutal force
class Solution {
public:
    int findCelebrity(int n) {
        for(int i = 0; i < n; i++){
            if(isCelebrity(n,i)){
                return i;
            }
        }
        return -1;
    }
    
    bool isCelebrity(int n, int i){
        for(int j = 0; j < n; j++){
            if(j == i){ // don't ask if i knows i
                continue;
            }
            // if i person knows someone, or someone doesn't know i
            // then i is not a celebrity
            if(knows(i,j) || !knows(j,i)){ 
                return false;
            }
        }
        return true;
    }
};