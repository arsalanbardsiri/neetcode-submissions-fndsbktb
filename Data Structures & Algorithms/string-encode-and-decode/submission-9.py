class Solution:
    def encode(self, strs: List[str]) -> str:
        # new_str = ""
        # for s in strs:
        #     new_str += f"{len(s)}~"+s
        # return new_str
        new_str = ""
        for word in strs:
            new_str += str(len(word))+"#"+word
        return (new_str)
    def decode(self, s: str) -> List[str]:
        # res = []
        # i = 0
        # while i < len(s):
        #     j = i
        #     while s[j] != "~": 
        #         j += 1
        #     length = int(s[i:j])
        #     i = j + 1 
        #     j = i + length 
            
        #     res.append(s[i:j])
        #     i = j
            
        # return res
        lst = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
                #4#neet4#code4#love3#you
                #^^
                #ij Exits the loop
            lent = int(s[i:j]) #give us the number
            i = j + 1
            j = i + lent
            lst.append(s[i:j])
            i = j
        return lst
            