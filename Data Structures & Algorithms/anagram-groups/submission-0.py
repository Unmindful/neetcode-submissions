class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs_dict = collections.defaultdict(list)
        for string in strs:
            count = [0]*26
            for char in string:
                count[ord(char) - ord('a')] += 1
            strs_dict[tuple(count)].append(string)
        return list(strs_dict.values())
