N, K = map(int, input().split())
coin_list = []
count = 0
for i in range(N):
    coin_list.append(int(input()))
for i in range(N - 1, -1, -1):
    if K == 0:
        break
    if coin_list[i] > K:
        continue
    count += K // coin_list[i]
    K %= coin_list[i]
print(count)