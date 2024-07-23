class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        c = Counter(nums)
        l = sorted(sorted(c.items(), key=lambda x: x[0], reverse=True), key=lambda x: x[1])
        out = []
        for i in l:
            out += [i[0]] * i[1]
        return out