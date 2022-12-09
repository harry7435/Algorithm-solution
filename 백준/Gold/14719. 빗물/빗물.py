import sys
input = sys.stdin.readline

h, w = map(int, input().split())
wall_list = list(map(int, input().split()))
rain = 0
# 양쪽 경계를 제외하고 빗물이 고이는 것을 체크
for i in range(1, w-1):
    # 왼쪽, 오른쪽 최대 높이 벽 구하기
    left_wall = max(wall_list[:i])
    right_wall = max(wall_list[i+1:])
    # 둘 중 작은 기준 벽 구하기
    min_wall = min(left_wall, right_wall)
    # 기준 벽보다 현재 벽이 낮으면 빗물이 고임
    if wall_list[i] < min_wall:
        rain += min_wall - wall_list[i]

print(rain)