class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        a = sorted(s)
        b = sorted(t)

        print(a,b)
        if (a == b):
            return True
        else:
            return False