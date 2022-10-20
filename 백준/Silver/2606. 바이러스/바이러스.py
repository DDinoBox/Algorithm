from collections import deque

N = int(input()) 
V = int(input()) 

graph = [[] for i in range(N+1)]
visited = [0] * (N+1)
for i in range(V):
    a,b = map(int,input().split())
    graph[a] += [b] 
    graph[b] += [a] 
visited[1] = 1 
Q = deque([1])
while Q:
    c = Q.popleft()
    for nx in graph[c]:
        if visited[nx] == 0:
            Q.append(nx)
            visited[nx] = 1
            
print(sum(visited)-1)