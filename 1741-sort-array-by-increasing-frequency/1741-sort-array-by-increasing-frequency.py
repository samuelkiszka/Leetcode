class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        l = sorted(sorted(Counter(nums).items(), key=lambda x: x[0], reverse=True), key=lambda x: x[1])
        out = []
        for i in l:
            out += [i[0]] * i[1]
        return out