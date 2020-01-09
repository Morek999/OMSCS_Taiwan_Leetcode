# Most Common Word
# https://leetcode.com/problems/most-common-word/

from typing import List

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = paragraph.lower().replace("!", " ").replace("?", " ")\
            .replace("'", " ").replace(",", " ").replace(";", " ").replace(".", " ").split()
        wordfreq = {}
        for i in paragraph:
            if i in wordfreq:
                wordfreq[i] += 1
            else:
                wordfreq[i] = 0
        for b in banned:
            wordfreq.pop(b, None)
        return max(wordfreq, key=wordfreq.get)

paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
print(Solution().mostCommonWord(paragraph, banned))