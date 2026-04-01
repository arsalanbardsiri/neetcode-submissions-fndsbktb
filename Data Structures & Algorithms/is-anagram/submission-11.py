class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        maps1 = {}
        i = 1
        maps2 = {}
        j = 1

        for letter in s:
            if letter in maps1:
                i = maps1[letter] + 1
            else:
                i = 1
            maps1[letter] = i
        
        for letter in t:
            if letter in maps2:
                j = maps2[letter] + 1
            else:
                j = 1
            maps2[letter] = j

        return maps1 == maps2    