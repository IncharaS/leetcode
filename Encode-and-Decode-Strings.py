class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        string = ''
        for s in strs:
            for i in s:
                if i == '/':
                    string += '/'
                string += i
            string += '/:'
        # print(string)

        return string

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        length = len(s)
        i = 0
        res = []
        string = ''
        while i < length:
            if s[i] == '/':
                # there are 2 options
                # 1. if / is next, it was just added to encode
                # 2. if : is next, it was delimiter
                i += 1
                if i < length and s[i] == ':':
                    res.append(string)
                    string = ''
                elif i < length and s[i] == '/':
                    string += '/'
                i += 1
            else:
                string += s[i]
                i += 1
            # print(string)
        return res




# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))