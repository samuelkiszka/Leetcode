class Solution:
    def minimumPushes(self, word: str) -> int:
        c = Counter(word)
        result = 0
        if len(c) < 9:
            result = len(word)
        else:
            multiplier = 1
            letters = c.most_common()
            while True:
                cycle = 0
                for letter in letters[8*(multiplier - 1):8*multiplier]:
                    result += letter[1] * multiplier
                    cycle += 1
                if cycle != 8:
                    break
                multiplier += 1
        return result