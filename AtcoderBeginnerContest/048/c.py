N, x = map(int, input().split())
nums = list(map(int, input().split()))
# print(nums)
ans = 0
for i in range(1, N):
    if nums[i - 1] + nums[i] > x:
        diff = nums[i - 1] + nums[i] - x
        if diff > nums[i]:
            nums[i - 1] -= (diff - nums[i])
            nums[i] = 0
        else:
            nums[i] -= diff
        ans += diff
# print(nums)
print(ans)
