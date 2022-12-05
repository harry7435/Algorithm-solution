import sys
input = sys.stdin.readline
import heapq

n = int(input())
heap = []
# 절댓값 힙 구현
for i in range(n):
    x = int(input())
    # x가 0이 아니면 힙에 추가, abs로 절댓값 기준으로 최소 정렬
    if x != 0:
        heapq.heappush(heap, (abs(x), x))
    else:
        # heap이 비어있는데 0이 입력되면 0출력
        if not heap:
            print(0)
        # 그 외 절댓값 최소값 출력
        else:
            print(heapq.heappop(heap)[1])