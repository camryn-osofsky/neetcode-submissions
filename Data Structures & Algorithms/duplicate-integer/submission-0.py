class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # initial thoughts: sort the list and iterate through, checking each element against the next
        # if there is a match, break and return true
        # if there is no match, return false
        nums.sort()
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return True

        return False

        