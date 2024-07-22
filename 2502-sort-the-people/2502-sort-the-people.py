class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        d = {heights[i]: names[i] for i in range(len(names))}
        h = sorted(heights)
        return [d[he] for he in h[::-1]]