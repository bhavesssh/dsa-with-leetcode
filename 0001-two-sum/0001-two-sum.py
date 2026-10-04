class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        list_dict = {}
        for index in range(len(nums)):
            complement = target - nums[index]
            if complement in list_dict:
                return [list_dict[complement], index]
            list_dict[nums[index]] = index
        return []