class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # sort the list alphabetically and check equality
        # first make sure they are the same length:
        if len(s) != len(t):
            return False

        # sort the lists alphabetically
        s = ''.join(sorted(s))
        t = ''.join(sorted(t))

        # check strings against each other
        if s == t:
            return True

        return False
