from sys import stdin


nums = list(stdin.readline().rstrip().split(':'))
if not nums[0]:
    nums.pop(0)
elif not nums[-1]:
    nums.pop()
ans = []
for num in nums:
    if not num:
        ans += ['0000'] * (9 - len(nums))
    else:
        ans.append(num.zfill(4))

print(':'.join(ans))

