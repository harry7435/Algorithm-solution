from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    # 2배를 곱해야 인접한 곳을 경로로 착각하지 않음
    field = [[-1 for _ in range(51 * 2)] for _ in range(51 * 2)]
    # 좌표 표시
    for rec in rectangle:
        xl, yl, xh, yh = map(lambda x: x*2, rec)
        for x in range(xl, xh+1):
            for y in range(yl, yh+1):
                # 내부는 0
                if xl < x < xh and yl < y < yh:
                    field[x][y] = 0
                # 내부는 아닌데 사각형 범위 안이면 테두리
                elif field[x][y] != 0:
                    field[x][y] = 1
    # 최단거리 bfs 수행
    queue = deque()
    queue.append([characterX*2, characterY*2])
    visited = [[0 for _ in range(51 * 2)] for _ in range(51 * 2)]
    visited[characterX*2][characterY*2] = 1
    # 상하좌우 이동 좌표
    dx = [-1, 1, 0, 0]
    dy = [0, 0 , -1, 1]
    
    while queue:
        x, y = queue.popleft()
        # 아이템에 도착하면 시작점 제외 후 2 나누기
        if x == itemX*2 and y == itemY*2:
            answer = (visited[x][y] - 1) // 2
            break
        # 테두리를 따라서 이동
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if visited[nx][ny] == 0 and field[nx][ny] == 1:
                queue.append([nx, ny])
                visited[nx][ny] = visited[x][y] + 1
                
    return answer