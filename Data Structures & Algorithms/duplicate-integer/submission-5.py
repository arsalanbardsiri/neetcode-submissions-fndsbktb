class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mps = {}
        #[2,3,4,2]
        for num in nums:
            if num in mps:
                return True
            mps[num] = mps.get(num,0)
        return False
