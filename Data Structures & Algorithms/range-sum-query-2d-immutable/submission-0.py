class NumMatrix:

    def __init__(self, matrix: List[List[int]]):        
        """
        Prefix - sum
        """
        self.matrix = matrix
        # self.prefix = []
        # sum_res = 0
        # for i,nums in enumerate(matrix):
        #     sum_res = sum(nums)
        #     self.prefix.append(sum_res)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        """
        [[[[3, 0, 1, 4, 2], 
           [5, 6, 3, 2, 1], 
           [1, 2, 0, 1, 5], 
           [4, 1, 0, 1, 7], 
           [1, 0, 3, 0, 5]]], 
           -----------------------------------------
           [2, 1, 4, 3], [1, 1, 2, 2], [1, 2, 2, 4]]
        """
        #4 corners
        # for i in range(4):
        #     a = [self.matrix[row1][col1],self.matrix[row1][col2],self.matrix[row2][col1],self.matrix[row2][col2]]
        # print(a)
        



        """
        row 1 will give an index which indicates which sub-array to look at
        col 1 in index of the element in the sub
        row 2 will give an index which indicates which sub-array to look at
        col 2 in index of the element in the sub
        
        The hurdle
        The sum is (6+3) 
                +  (2+0)
                  -------
                    11 
        So, |Row2 - Row1| + 1  = number of Sub-Arr s
        and form col1 to col2 is the elements to add
        So for,[2, 1, 4, 3] => 4-2 = 2+1, 3 sub arrays
        range of elemenst from 1 to 3
        2, 0, 1
        1, 0, 1 => 2+1+1+1+3 = 8
        0, 3, 0
        """
        tot = 0
        number_of_subarr_to_cover = abs(row2-row1) + 1
        for row in range(row1,row2+1):
            tot += (sum(self.matrix[row][col1:col2+1]))
        
        return tot

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
# 