class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        dic = [(heights[i], names[i]) for i in range(len(names))]
        dic.sort(key=lambda x: x[0])
        return [p[1] for p in dic[::-1]]