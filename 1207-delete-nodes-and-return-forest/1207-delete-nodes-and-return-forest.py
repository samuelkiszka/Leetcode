# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        res = {root.val: root}
        to_delete: set(to_delete)

        def recursion(parent, cur, isleft):
            nonlocal res
            if not cur:
                return

            recursion(cur, cur.left, True)
            recursion(cur, cur.right, False)

            if cur.val in to_delete:
                if cur.val in res:
                    del res[cur.val]

                if parent:
                    if isleft:
                        parent.left = None
                    else:
                        parent.right = None

                if cur.left:
                    res[cur.left.val] = cur.left
                if cur.right:
                    res[cur.right.val] = cur.right

        recursion(None, root, False)
        return res.values()