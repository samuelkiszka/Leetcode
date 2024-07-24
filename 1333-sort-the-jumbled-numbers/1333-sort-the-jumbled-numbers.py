class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        l = len(nums)
        d = {
            i: mapping[i] for i in range(len(mapping))
        }

        mapped = []
        for i in range(l):
            s = str(nums[i])
            out = ""
            for c in s:
                out += str(d[int(c)])
            mapped += [(int(out), i)]

        mapped = sorted(mapped, key=lambda x: x[0])
        return [nums[mapped[i][1]] for i in range(l)]