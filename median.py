class Solution:
    def findMedianSortedArrays(self, param_1: list[int], param_2: list[int]):
        merged_nums = param_1 + param_2
        sorted_merged_nums = sorted(merged_nums)

        length = len(sorted_merged_nums)
        
        median = 0
        
        if length % 2 == 1:
            median = sorted_merged_nums[int(length / 2)]
        else:
            median = (sorted_merged_nums[int(length / 2) - 1] + sorted_merged_nums[int(length / 2)]) / 2

        return median