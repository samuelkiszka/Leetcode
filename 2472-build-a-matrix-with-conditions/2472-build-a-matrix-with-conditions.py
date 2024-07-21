class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        row_conds = set((i[0], i[1]) for i in rowConditions)
        col_conds = set((i[0], i[1]) for i in colConditions)
        res = [[0] * k for _ in range(k)]
        pos = {i: [0, 0] for i in range(k + 1)}

        # sort rows
        r = [0] * k
        deps = {i: set() for i in range(k + 1)}
        for c in row_conds:
            r[c[1] - 1] += 1
            deps[c[0]].add(c[1])
        
        stack = []
        for i in range(k):
            if not r[i]:
                stack.append(i + 1)
        
        row_order = []
        while stack:
            cur = stack.pop(0)
            row_order.append(cur)
            for dep in deps[cur]:
                r[dep - 1] -= 1
                if not r[dep - 1]:
                    stack.append(dep)

        if len(row_order) != k:
            return []

        # sort cols
        cols = [0] * k
        deps = {i: set() for i in range(k + 1)}
        for c in col_conds:
            cols[c[1] - 1] += 1
            deps[c[0]].add(c[1])

        stack = []
        for i in range(k):
            if not cols[i]:
                stack.append(i + 1)

        col_order = []
        while stack:
            cur = stack.pop(0)
            col_order.append(cur)
            for dep in deps[cur]:
                # print(f"{cur} -> {dep}")
                cols[dep - 1] -= 1
                if not cols[dep - 1]:
                    stack.append(dep)

        if len(col_order) != k:
            return []

        for i in range(k):
            pos[row_order[i]][0] = i
            pos[col_order[i]][1] = i

        for i in range(k + 1):
            # print(i)
            res[pos[i][0]][pos[i][1]] = i

        return res