N = int(input())
nums = input().split()

for i in range(len(nums)):
    for j in range(len(nums) - 1 - i):
        if nums[j] + nums[j+1] < nums[j+1] + nums[j]:
            nums[j], nums[j+1] = nums[j+1], nums[j]

answer = ''.join(nums)
print('0' if answer[0] == '0' else answer)
