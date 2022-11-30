import sys
input = sys.stdin.readline

computer = int(input())
connect = int(input())
graph = [[] for _ in range(computer+1)]
visited = [False for _ in range(computer+1)]
# 그래프
for i in range(connect):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# dfs 재귀, 스택 이용
virus = 0
def dfs(start):
    global virus
    visited[start] = True
    for com in graph[start]:
        if visited[com] == False:
            dfs(com)
            virus += 1

dfs(1)
print(virus)

# bfs 큐 사용
# virus = 0
# def bfs(start):
#     global virus
#     queue = []
#     queue.append(start)
#     while queue:
#         com = queue.pop(0)
#         visited[com] = True
#         for i in graph[com]:
#             if visited[i] == False:
#                 visited[i] = True
#                 queue.append(i)
#                 virus += 1

# bfs(1)
# print(virus)