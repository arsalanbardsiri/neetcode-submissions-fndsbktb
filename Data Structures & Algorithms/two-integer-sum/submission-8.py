class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapofnudes = {}

        for i,n in enumerate(nums):
            differance = target - n

            if differance in mapofnudes:
                return [mapofnudes[differance],i]
            
            mapofnudes[n] = i
        return[]