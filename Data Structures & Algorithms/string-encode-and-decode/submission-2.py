class Solution:

    def encode(self, strs: List[str]) -> str:

        if not strs:
            return ''

        encoded_strs = []

        for s in strs:
            encoded_strs.append(str(len(s)))
            encoded_strs.append(',')
        encoded_strs.append('#')
        encoded_strs.extend(strs)
        return ''.join(encoded_strs)


    def decode(self, s: str) -> List[str]:
        if not s:
            return []

        lens = []
        res = []
        num = ''

        for i, char in enumerate(s):
            if char == '#':
                i += 1
                break
            elif char == ',':
                lens.append((int(num)))
                num = ''
            else:
                num += char

        for len in lens:
            res.append(s[i:i+len])
            i += len
        return res

            

