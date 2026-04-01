class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # if len(s) != len(t):
        #     return False
        # #"NO"
        # map_s = {}
        # #"ON"
        # map_t = {}
        # for char in s:
        #     # inital {"N": 0} then + 1 => {"N": 1}
        #     map_s[char] = map_s.get(char, 0) + 1
    
        # for char in t:
        #     map_t[char] = map_t.get(char, 0) + 1
        # return map_s == map_t

        mps1 = {}
        mps2 = {}

        for char in s:
            mps1[char] = mps1.get(char,0)+1

        for char in t:
            mps2[char] = mps2.get(char,0)+1
        return mps1 == mps2 