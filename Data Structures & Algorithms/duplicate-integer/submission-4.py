class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # nums_ = {}
        # i = 1
        
        # for i,num in enumerate(nums):
        #     if num in nums_:
        #         return True
        #     nums_[num] = i
        # return False
        mps = {}
        i = 0

        for num in nums:
            if num in mps:
                print("before true", mps)
                return True
            mps[num] = i
        print("before false", mps)
        return False