class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
      mapOfNums = {}
      for i, n in enumerate(nums):
        diff = target - n
        if diff in mapOfNums:
            return [mapOfNums[diff],i]
        mapOfNums[n] = i
      return[]