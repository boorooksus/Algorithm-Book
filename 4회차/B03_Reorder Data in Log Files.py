from typing import List


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letters, digits = [], []
        for log in logs:
            if log[-1].isdigit():
                digits.append(log)
            else:
                letters.append(list(log.split()))

        letters.sort(key=lambda x: (x[1:], x[0]))
        return list(' '.join(letter) for letter in letters) + digits
    
