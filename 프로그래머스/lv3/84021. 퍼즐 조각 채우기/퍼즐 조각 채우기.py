import copy
# 상하좌우 이동 좌표
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
# 도형 찾기
def dfs(x, y, graph, pos, n, find_num):
    result = [pos]  # 기준점 저장
    # 상하좌우 중 찾는 숫자로 이어나가기
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        new_pos = [pos[0] + dx[i], pos[1] + dy[i]]
        
        if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == find_num:
            graph[nx][ny] = 2
            result = result + dfs(nx, ny, graph, new_pos, n, find_num)
            
    return result
# 시계방향 90도 회전
def rotation(block):
    n = len(block)
    new_block = [[0 for _ in range(n)] for _ in range(n)]
    
    for x in range(n):
        for y in range(n):
            # 각 좌표에 대해서 치환
            new_block[y][n-x-1] = block[x][y]
            
    return new_block

def solution(game_board, table):
    answer = 0
    n = len(game_board)
    # 보드 복사
    copy_board = copy.deepcopy(game_board)
    blocks = []
    # 보드 내 도형 찾기
    for x in range(n):
        for y in range(n):
            # 보드에서 비어있는 칸일 경우
            if copy_board[x][y] == 0:
                copy_board[x][y] = 2
                # 첫번째는 [0,0] 출발점이므로 제외
                block = dfs(x, y, copy_board, [0, 0], n, 0)[1:]
                blocks.append(block)
    # 테이블 회전
    for rot in range(4):
        table = rotation(table)
        copy_table = copy.deepcopy(table)
        # 테이블 내 도형 찾기
        for x in range(n):
            for y in range(n):
                # 테이블에서 1이면 도형
                if copy_table[x][y] == 1:
                    # 보드와 마찬가지 방법 사용
                    copy_table[x][y] = 2
                    table_block = dfs(x, y, copy_table, [0, 0], n, 1)[1:]
                    # 일치할 경우
                    if table_block in blocks:
                        blocks.pop(blocks.index(table_block))
                        # [0,0]도 퍼즐 조각 갯수로 추가 +1
                        answer += (len(table_block)+1)
                        # 테이블 업데이트
                        table = copy.deepcopy(copy_table)
                    # 일치하지 않을 경우 테이블 원상복귀
                    else:
                        copy_table = copy.deepcopy(table)
                    
    return answer