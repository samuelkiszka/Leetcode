class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        c = Counter(nums)
        l = sorted(c.items(), key=lambda x: (x[1], -x[0]))
        out = []
        for i in l:
            out += [i[0]] * i[1]
        return out