class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # make a hashmap using the sorted strings as keys and their indices as values
        # initialize hashmap
        myMap = {}

        # loop through strings, sort, and add to the map
        for s in strs:
            sortedStr = ''.join(sorted(s))
            if sortedStr in myMap:
                myMap[sortedStr].append(s)
            else:
                myMap[sortedStr] = [s]

        # return the values as a list (will format as a 2D array)
        return list(myMap.values())
