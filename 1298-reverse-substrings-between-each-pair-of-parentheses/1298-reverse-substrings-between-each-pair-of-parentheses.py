class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = [""]
        l = 0
        while l < len(s):
            if s[l] ==  '(':
                stack.append("")
            elif s[l] == ')':
                stack[-2] += stack[-1][::-1]
                stack.pop(-1)
            else:
                stack[-1] += s[l]
            l += 1
        return stack[-1]
