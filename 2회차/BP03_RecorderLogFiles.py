from typing import List

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        lets, digs = [], []
        for log in logs:
            # log = log.split()
            if log.split()[1].isdigit():
                digs.append(log)
            else:
                lets.append(log)

        lets.sort(key=lambda x: (x.split()[1:], x.split()[0]))
        return lets + digs
