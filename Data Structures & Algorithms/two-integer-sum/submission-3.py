class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # make a hash map mapping each value to a list of its indices
        # while passing through, check if the complementary value exists in the map already
        # if yes, return
        # if not, keep going
        
        # initialize hashmap
        myMap = {}

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in myMap:
                return [myMap[diff][0], i]
            else:
                myMap[nums[i]] = [i]

