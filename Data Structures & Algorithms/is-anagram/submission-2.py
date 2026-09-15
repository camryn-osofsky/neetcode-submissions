class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # sort the list alphabetically and check equality
        # first make sure they are the same length:
        if len(s) != len(t):
            return False

        # check strings against each other
        if sorted(s) == sorted(t):
            return True

        return False
