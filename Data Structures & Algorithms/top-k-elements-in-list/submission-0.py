class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_freq = Counter(nums).most_common(k)
        elements = [el[0] for el in nums_freq]

        return elements

