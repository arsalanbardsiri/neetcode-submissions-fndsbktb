class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        mps_s = {}
        mps_t = {}

        for char in s:
             mps_s[char] = mps_s.get(char,0)+1
        for char in t:
             mps_t[char] = mps_t.get(char,0)+1
        return mps_s == mps_t