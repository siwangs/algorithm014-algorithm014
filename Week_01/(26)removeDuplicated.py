class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        uniq_index = 0

        for left in range(len(nums))[1:]:
            if nums[uniq_index] != nums[left]:
                uniq_index += 1
                nums[uniq_index] = nums[left]

        return uniq_index + 1
