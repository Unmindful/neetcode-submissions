from collections import Counter
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        counts = Counter(nums)
        return max(counts.values()) > 1 if counts.values() else False
