from typing import List


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letters, digits = [], []
        for log in logs:
            letters.append(log) if log[-1].isalpha() else digits.append(log)

        letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))

        return letters + digits


print(Solution().reorderLogFiles(["dig1 8 1 5 1","let2 own kit dig","let1 art can","dig2 3 6","let3 art zero"]))
