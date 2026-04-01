class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # nums_freq = Counter(nums).most_common(k)
        # #comprehension
        # elements = [el[0] for el in nums_freq]

        # return elements

        nums_frq = Counter(nums).most_common(k)
        print(nums_frq)
        elements = [el[0] for el in nums_frq]
        return elements