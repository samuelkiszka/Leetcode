class Solution:
    def numberToWords(self, num: int) -> str:
        if not num:
            return "Zero"
        nums = {
            1: ["One", "Eleven" , None],
            2: ["Two", "Twelve", "Twenty"],
            3: ["Three", "Thirteen", "Thirty"],
            4: ["Four", "Fourteen", "Forty"],
            5: ["Five", "Fifteen", "Fifty"],
            6: ["Six", "Sixteen", "Sixty"],
            7: ["Seven", "Seventeen", "Seventy"],
            8: ["Eight", "Eighteen", "Eighty"],
            9: ["Nine", "Nineteen", "Ninety"],
            0: [None, "Ten", "Hundred"],
        }
        orders = ["Thousand", "Million", "Billion"]
        out = []
        order = 0
        while num:
            l = len(out)
            act = num % 1000
            tens = act % 100
            if tens:
                if tens < 10:
                    out.append(nums[tens][0])
                elif tens < 20:
                    out.append(nums[tens % 10][1])
                else:
                    if tens % 10:
                        out.append(nums[tens % 10][0])
                    if tens // 10:
                        out.append(nums[tens // 10][2])
            hund = act // 100
            if hund:
                out.append(nums[0][2])
                out.append(nums[hund][0])
            num = num // 1000
            if order and l != len(out):
                out.insert(l, orders[order-1])
            order += 1
        return " ".join(out[::-1])