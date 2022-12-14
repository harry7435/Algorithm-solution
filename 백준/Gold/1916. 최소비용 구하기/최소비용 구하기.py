import sys
import heapq
from sys import maxsize
input = sys.stdin.readline
INF = maxsize
# 다익스트라 알고리즘 사용
def get_min_dist(start):
    # 처음 위치 거리 0, 이동 큐에 초기 위치 추가
    dist[start] = 0
    queue = []
    heapq.heappush(queue, (0, start))
    # 현재 위치에서 최소 거리로 가는 경우 체크
    while queue:
        # 현재 위치 정보 가져오기
        current_dist, current_loc = heapq.heappop(queue)   
        # 현재까지 거리보다 기존에 있는 거리가 더 짧으면 패스
        if current_dist > dist[current_loc]: continue
        
        for city in cities[current_loc]:
            cost = city[1] + current_dist   # 해당 도시를 지날 때 거리
            # 기존 거리보다 짧으면 갱신
            if cost < dist[city[0]]:
                dist[city[0]] = cost
                # 다음 이동 큐에 추가
                heapq.heappush(queue, (dist[city[0]], city[0]))

n = int(input())
m = int(input())
dist = [INF for _ in range(n+1)] 
cities = [[] for _ in range(n+1)]
for i in range(m):
    start, end, cost = map(int, input().split())
    cities[start].append((end, cost))

start, end = map(int, input().split())

get_min_dist(start)

print(dist[end])