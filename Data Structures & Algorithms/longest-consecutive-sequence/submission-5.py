class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if len(nums) == 0:
            return 0

        nums.sort()
        currCount = 1
        maxCount = 1
        print(nums)

        for i in range(len(nums) - 1):
            if nums[i] + 1 == nums[i + 1]:
                currCount += 1
            elif nums[i] == nums[i + 1]:
                continue
            else:
                maxCount = max(maxCount, currCount)
                currCount = 1

        return max(maxCount, currCount)