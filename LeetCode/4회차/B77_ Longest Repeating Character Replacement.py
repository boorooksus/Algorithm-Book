from collections import Counter


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        cnt = Counter()
        left = 0
        res = 0

        for right, char in enumerate(s):
            cnt[char] += 1

            if right - left + 1 <= k:
                continue

            while left < right and \
                    (len(cnt.values()) >= 2 and right - left + 1 - cnt.most_common(1)[0][1] > k):
                cnt[s[left]] -= 1
                left += 1

            res = max(res, right - left + 1)

        return res


print(Solution().characterReplacement("KRSCDCSONAJNHLBMDQGIFCPEKPOHQIHLTDIQGEKLRLCQNBOHNDQGHJPNDQPERNFSSSRDEQLFPCCCARFMDLHADJADAGNNSBNCJQOF"
,4))