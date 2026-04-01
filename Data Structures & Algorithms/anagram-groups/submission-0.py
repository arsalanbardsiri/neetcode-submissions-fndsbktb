class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        maps = defaultdict(list)

        for word in strs:
            key = sorted(word)

            maps[str(key)].append(word)

        return(list(maps.values()))    