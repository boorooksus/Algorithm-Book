from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grp = defaultdict(list)
        for word in strs:
            grp[''.join(sorted(word))].append(word)
        return grp.values()



sol = Solution()
sol.groupAnagrams(["eat","tea","tan","ate","nat","bat"])