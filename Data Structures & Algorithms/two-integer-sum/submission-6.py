class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # indx = []
        # if nums == [5,5]:
        #     arr1 = [0,1]
        #     return arr1


        # for i in range(len(nums)):
        #     m = target - nums[i]
        #     if m in nums:
        #         indx.append(i)
        #         indx.append(nums.index(m))
        #         break
        # return indx
        mapofmydick = {}

        for index, value in enumerate(nums):
            t = target - value
            if t in mapofmydick:
                return[mapofmydick[t],index]
            mapofmydick[value] = index
        return[]
        
            