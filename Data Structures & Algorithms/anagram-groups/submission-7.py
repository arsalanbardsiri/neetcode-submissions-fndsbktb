class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #What defaultdict does if key not in creates the case for it
        #if in it adds to it
        # mps = defaultdict(list)

        # for word in strs:
        #     key = sorted(word)
        #     mps["".join(key)].append(word)
        # return list(mps.values())

        mps = defaultdict(list)
        
        for word in strs:
            count = [0] * 26
            for char in word:
                count[ord(char) - ord('a')] += 1
            mps[str(count)].append(word)
        return list(mps.values())