class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # 2 pointers:
        # move outside in, if i + j > target, move j inwards
        # else, increment i

        i = 0
        j = len(numbers) - 1

        while (i < j):
            if numbers[i] + numbers[j] == target:
                break
            elif numbers[i] + numbers[j] > target:
                j -= 1
            else:
                i += 1
            
        # return the array, adding 1 to make it 1-indexed
        return [i + 1, j + 1]
        
        
        