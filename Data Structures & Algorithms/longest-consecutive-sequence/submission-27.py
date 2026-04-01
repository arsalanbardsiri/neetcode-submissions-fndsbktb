class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
#intial
        # if len(nums) == 0:
        #     return 0
        # sets = set(nums)
        # #The problem
        # counter = 1
        # # is_4_or_more = len(set) > 3 #n-1 n n+1 n+2
        # for num in sets:
        #     # is_4_or_more_ = (num-1 in sets)and(num+1 in sets)and(num+2 in sets)
        #     if num+1 in sets:
        #         counter +=1
        # return counter
        sets = set(nums)
        fnl_count = 0

        if  len(nums) == 0:
            return 0
        #set does not seem to be orderd
        #no doubles
        for num in sets:
            #begin of Consecutive
            if (num - 1) not in sets:
                cur_num = num
                count = 1

                while cur_num + 1 in sets:
                    cur_num+=1
                    count += 1
                fnl_count = max(fnl_count,count)
        return fnl_count
