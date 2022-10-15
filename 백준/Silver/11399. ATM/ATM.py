N = int(input())
nums = []
total = 0
cur = 0
nums = list(map(int, input().split()))

nums.sort()
for i in nums:
    cur += i
    total += cur
print(total)