class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        def get_order(conds):
            counts = [0] * k
            deps = {i: set() for i in range(k + 1)}
            for c in conds:
                counts[c[1] - 1] += 1
                deps[c[0]].add(c[1])
            
            stack = []
            for i in range(k):
                if counts[i] == 0:
                    stack.append(i + 1)
            
            order = []
            while stack:
                cur = stack.pop(0)
                order.append(cur)
                for dep in deps[cur]:
                    counts[dep - 1] -= 1
                    if not counts[dep - 1]:
                        stack.append(dep)
            
            return order if len(order) == k else None

        row_conds = set((i[0], i[1]) for i in rowConditions)
        col_conds = set((i[0], i[1]) for i in colConditions)

        row_order = get_order(row_conds)
        col_order = get_order(col_conds)

        if not row_order or not col_order:
            return []

        pos = {i: [0, 0] for i in range(k + 1)}
        for i in range(k):
            pos[row_order[i]][0] = i
            pos[col_order[i]][1] = i

        res = [[0] * k for _ in range(k)]
        for i in range(k + 1):
            res[pos[i][0]][pos[i][1]] = i

        return res