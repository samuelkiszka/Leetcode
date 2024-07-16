# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        
        def search(needed, node):
            if not node:
                return ""
            elif node.left and node.left.val == needed:
                return "L"
            elif node.right and node.right.val == needed:
                return "R"
            else:
                l_path = search(needed, node.left)
                r_path = search(needed, node.right)
                if l_path:
                    return f"L{l_path}"
                elif r_path:
                    return f"R{r_path}"
                else:
                    return ""

        start = search(startValue, root)
        dest = search(destValue, root)
        
        p = 0
        l = len(start) if len(start) < len(dest) else len(dest)

        for i in range(l):
            if start[i] == dest[i]:
                p += 1
            else:
                break

        start = "U" * (len(start) - p)
        return f"{start}{dest[p:]}"

        