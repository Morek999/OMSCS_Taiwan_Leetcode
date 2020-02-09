/*
The method I came out is very simple. Two cases can be found here:

1. this number is happy number
Ex. 7 -> 49 -> 97 -> 130 -> 10 -->1 
2. this number is not happy number and it will go into a cycle
Ex. 116 -> 38 -> 73 -> 58 -> 89 -> 145 -> 42 -> 20 -> 4 -> 16 -> 37 -> 58(cycle)

So I just use a hashset to detect a cycle and write a simple function to get the next number.
If there's a cycle or I get n == 1 then I jump out of the loop, then check if n == 1

Time complexity: O(log n) 
This is the most interesting part of this question. 
For the number with 3 digits, it's impossible to get more than 243, check the table on the leetcode.

First, suppose we have an number n that has d digit, then it will satisfy the inequalities below:
10 ^(d-1) <= n < 10 ^(d)
by taking log to two sides --> d-1 <= log(n) < d --> so getNext will take O(logn) time complexity for any given number n

Every time we process a number N, it will take log(N), however since for number beyond 243 everytime it will lose one digit or more, 
so the dominate time complexity will be log(n), where n is the original number.

Space complexity: O(log(n))

Think about what would happen if you had a number with 1 million digits in it. 
The first step of the algorithm would process those million digits, and then the next value would be, at most (pretend all the digits are 9), 
be 81 * 1,000,000 = 81,000,00081∗1,000,000=81,000,000. In just one step, we've gone from a million digits, down to just 8. 
The largest possible 8 digit number we could get is 99,9999,99999,9999,999, which then goes down to 81 * 8 = 64881∗8=648. 
And then from here, the cost will be the same as if we'd started with a 3 digit number. 
Starting with 2 million digits (a massively larger number than one with a 1 million digits) would only take roughly twice as long, as again, 
the dominant part is summing the squares of the 2 million digits, and the rest is tiny in comparison.

*/ 
class Solution {
public:
    bool isHappy(int n) {
        while(n != 1 && m.find(n)== m.end()){
            m.insert(n);
            n = getNext(n);
        }
        return n == 1;
    }
private:
    unordered_set<int> m;
    int getNext(int n){
        int total = 0;
        while(n){
            int d = n % 10;
            n /= 10;
            total += d*d;
        }
        return total;
    }
};