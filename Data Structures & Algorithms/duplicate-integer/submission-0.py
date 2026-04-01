class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        maps = {}
        for i,n in enumerate(nums):
            if n not in maps:
                i = 1
            else:
                i += 1
            maps[n] = i
        has_dup = any(num > 1 for num in maps.values())
        return(has_dup)