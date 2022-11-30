from collections import deque
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
min_time = [0 for _ in range(100001)]
# bfs 최소 시간이므로
def bfs(start, k):
    queue = deque([start])
    while queue:
        location = queue.popleft()
        move = [location-1, location+1, location*2]
        if location == k:
            print(min_time[location])
            break
        # 이동 가능한 경우의 수 다 따져보기
        for m in move:
            # 이동 좌표가 범위 내이고, 이전에 이동하지 않은 곳이어야 함(최소 경로)
            if 0 <= m <= 100000 and min_time[m] == 0:
                min_time[m] = min_time[location] + 1
                queue.append(m)

bfs(n, k)