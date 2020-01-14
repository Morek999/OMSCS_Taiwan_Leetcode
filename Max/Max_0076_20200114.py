""" 
76. Minimum Window Substring
https://leetcode.com/problems/minimum-window-substring/
Time complexity: O(J+S)
Space complexity: O(S)
Solution: 
 """

from typing import List
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        T = {}
        for i in list(t):
            T[i] = T[i] + 1 if i in T else 1
        required = len(T)
        l = r = track = 0
        window = {}
        ans = float('inf'), 0, 0
        while r < len(s):
            char = s[r]
            window[char] = window.get(char, 0) + 1
            if (char in T) and (window[char] == T[char]):
                track += 1
            while (l <= r) and (track == required):
                char = s[l]
                if r - l + 1 < ans[0]:
                    ans = (r - l + 1, l, r)
                window[char] -= 1
                if (char in T) and (window[char] < T[char]):
                    track -= 1
                l += 1
            r += 1
        return "" if ans[0] == float('inf') else s[ans[1]:ans[2]+1]

            
"""         def find_range(arr):
            return arr[max(arr, key=arr.get)] - arr[min(arr, key=arr.get)]
        T = list(t)
        holding = []
        marker = {}
        for n, i in enumerate(list(s)):
            print(marker)
            if i in T:
                if i in marker:
                    if len(marker) == 3:
                        tmp = marker.copy()
                        tmp[i] = n
                        print(f'{find_range(marker)} -> {tmp}')
                        if find_range(tmp) < find_range(marker):
                            marker[i] = n
                    else:
                        marker[i] = n
                else:
                    marker[i] = n
        return s[marker[min(marker, key=marker.get)] : marker[max(marker, key=marker.get)]] """

ans = [
    {"s":"ADOBECODEBANC", "t":"ABC"}    # output: "BANC"
]
for trails in ans:
    print(Solution().minWindow(**trails))
