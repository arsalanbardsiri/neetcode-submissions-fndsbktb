class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        track_of_sum = {}
        #target is 7 and the list is [5,6,3,4]
        
        for i,num in enumerate(nums):
            # 2 = 7 - 5
            diff = target - num
            # while on 5, 2 has been seen
            if diff in track_of_sum:

                return [track_of_sum[diff],i]
            track_of_sum[num] = i

        return []