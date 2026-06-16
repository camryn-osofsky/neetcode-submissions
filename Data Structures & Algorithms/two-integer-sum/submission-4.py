class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # make a hash map mapping each value to a list of its indices
        # while passing through, check if the complementary value exists in the map already
        # if yes, return
        # if not, keep going
        
        # initialize hashmap
        myMap = {}

        # loop through the list
        for i in range(len(nums)):
            # find the complementary value
            diff = target - nums[i]
            if diff in myMap: # is the complement in the hashmap?
                return [myMap[diff][0], i] # yes, we have our pair!
            else:
                myMap[nums[i]] = [i] # no, add this value and keep going

