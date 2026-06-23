class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # intuition: iterate thorugh the list and make a running product of the numbers
        # then, when building the solution list, simply divide the product by that number
        
        # count zeros to handle cases with multiple zeros
        zero_count = nums.count(0)
        # initialize product variable with 1 (anything * 1 is itself)
        product = 1
        # find the total product (excluding any 0s)
        for num in nums:
            if num != 0:
                product *= num
        # initialize result array
        result = []
        # iterate through the array, appending the result to the array
        for num in nums:
            # handle 0 case- append the product of all other nums
            if num == 0:
                if zero_count > 1: # handle several 0 case
                    result.append(0)
                else:
                    result.append(product)
            # handle non-zero case when a 0 exists in the list- append 0
            elif zero_count > 0:
                result.append(0)
            # handle all other cases- append the division result
            else:
                result.append(product//num)

        return result