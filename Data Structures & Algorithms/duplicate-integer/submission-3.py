class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_ = {}
        i = 1
        
        for i,num in enumerate(nums):
            if num in nums_:
                return True

            nums_[num] = i
        return False
