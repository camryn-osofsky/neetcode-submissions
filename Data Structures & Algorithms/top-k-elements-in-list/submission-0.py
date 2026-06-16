class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # make a hashmap of the elements and their frequencies by iterating through and adding to the value for each instance
        # make a sorted array of freq, num pairs
        # pop the last k items into a results array and return
        
        myMap = {}

        for num in nums:
            if num in myMap:
                myMap[num] += 1
            else:
                myMap[num] = 1
        
        pairArr = []
        for num, freq in myMap.items():
            pairArr.append([freq, num])

        pairArr.sort()

        result = []
        while len(result) < k:
            result.append(pairArr.pop()[1])

        return result

        
        