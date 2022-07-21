from typing import List


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letters, digits = [], []
        for log in logs:
            temp = log.split()
            if temp[1].isalpha():
                letters.append(temp)
            else:
                digits.append(log)
        letters.sort(key=lambda x: (x[1:], x[0]))
        return list(' '.join(i) for i in letters) + digits
