from collections import Counter


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        cnt = Counter()
        left = 0

        for right in range(1, len(s) + 1):
            cnt[s[right - 1]] += 1

            if right - left - cnt.most_common(1)[0][1] > k:
                cnt[s[left]] -= 1
                left += 1

        return right - left


print(Solution().characterReplacement("KRSCDCSONAJNHLBMDQGIFCPEKPOHQIHLTDIQGEKLRLCQNBOHNDQGHJPNDQPERNFSSSRDEQLFPCCCARFMDLHADJADAGNNSBNCJQOF"
,4))