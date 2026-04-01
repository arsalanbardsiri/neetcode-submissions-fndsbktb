class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #What defaultdict does if key not in creates the case for it
        #if in it adds to it
        # maps = defaultdict(list)

        # for word in strs:
        #     key = sorted(word)
        #     maps[str(key)].append(word)

        # return(list(maps.values()))

        mps = defaultdict(list)

        for word in strs:
            key = sorted(word)
            mps["".join(key)].append(word)
        return list(mps.values())