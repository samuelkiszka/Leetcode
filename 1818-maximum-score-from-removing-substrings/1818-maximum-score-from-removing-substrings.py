class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        if x > y:
            first, fp = "ab", x
            second, sp = "ba", y
        else:
            first, fp = "ba", y
            second, sp = "ab", x
        p = 0
        stack = [""]
        for i in range(len(s)):
            c = s[i]
            if c == first[1] and stack[-1] == first[0]:
                stack.pop()
                p += fp
            else:
                stack.append(c)
        stack_2 = [""]
        for i in range(len(stack)):
            c = stack[i]
            if c == second[1] and stack_2[-1] == second[0]:
                stack_2.pop()
                p += sp
            else:
                stack_2.append(c)
        return p
