class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_index_map = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in nums_index_map:
                return [nums_index_map[diff], i]
            nums_index_map[num] = i