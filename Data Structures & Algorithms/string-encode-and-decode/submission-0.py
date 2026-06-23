class Solution:

    def encode(self, strs: List[str]) -> str:
        # initialize the encoded string as empty
        encoded_str = ""
        # iterate through the list, concatenating the length, delimeter ($), and string
        for s in strs:
            encoded_str += str(len(s)) + "$" + s
        return encoded_str

    def decode(self, s: str) -> List[str]:
        # initialize the decoded list as empty
        decoded_str = []
        # initialize the iteration variable
        i = 0
        # outer loop moving through the length of the string
        while i < len(s):
            # initialize pointer j
            j = i
            # check if the current char matches the chosen delimeter ($), if not then increment
            while s[j] != "$":
                j += 1
            # i->j contains the length of the string (from encoding formula)- extract it
            segment_length = int(s[i:j])
            # move i to the start of the string
            i = j + 1
            # move j to the end of the string
            j = i + segment_length
            # append the slice of the encoded string that corresponds to the actual word
            decoded_str.append(s[i : j])
            # move i up to continue through the string
            i = j

        return decoded_str
        

