class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mps = {}

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in mps:
                print(diff,nums[i])
                return [mps[diff],i]
            mps[nums[i]] = mps.get(nums[i],i)
        return[]
        
