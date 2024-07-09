class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        t = 0
        w = 0
        for c in customers:
            if t <= c[0]:
                w += c[1]
                t = c[0] + c[1]
            else:
                w += c[1] + t - c[0]
                t += c[1]
        return w/len(customers)



        return 0.0