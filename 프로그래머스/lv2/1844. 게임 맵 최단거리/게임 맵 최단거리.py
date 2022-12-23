from collections import deque
# deque bfs 최단거리이므로
def solution(maps):
    answer = 0
    # 상 하 좌 우 이동좌표
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    # 지도 최대 행열
    row = len(maps)
    col = len(maps[0])
    # bfs 이동 큐
    queue = deque()
    queue.append([0, 0])
    # 최소 이동거리 2차원 배열
    min_distance = [[-1 for _ in range(col)] for _ in range(row)]
    min_distance[0][0] = 1  # 출발점 1
    # bfs 수행
    while queue:
        loc_row, loc_col = queue.popleft()  # 현재 좌표 추출
        # 상 하 좌 우 이동
        for i in range(4):
            new_loc_row = loc_row + dy[i]
            new_loc_col = loc_col + dx[i]
            # 지도 범위를 벗어나지 않고 이동 가능한 곳일 경우
            if 0 <= new_loc_row < row and 0 <= new_loc_col < col and maps[new_loc_row][new_loc_col] == 1:
                # 지나지 않은 곳일 경우
                if min_distance[new_loc_row][new_loc_col] == -1:
                    min_distance[new_loc_row][new_loc_col] = min_distance[loc_row][loc_col]+1   # 이전 최소 거리 + 1 갱신
                    queue.append([new_loc_row, new_loc_col])    # 큐 추가

    answer = min_distance[row-1][col-1] # 상대 팀 진영 최소 이동거리 출력
    return answer