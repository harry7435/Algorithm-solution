def dfs(n, computers, start, visited):
    visited[start] = True   # 시작 노드 방문
    for computer in range(n):
        # 본인이 아니며 연결된 컴퓨터일 경우
        if computer != start and computers[start][computer] == 1:
            # 지나지 않은 컴퓨터일 경우 더 탐색
            if visited[computer] == False:
                dfs(n, computers, computer, visited)
    
def solution(n, computers):
    answer = 0
    visited = [False for _ in range(n)]
    # 탐색 시작
    for idx in range(n):
        # 방문하지 않은 노드일 경우
        if visited[idx] == False:
            # 탐색이 마친 후 네트워크 갯수 +1
            dfs(n, computers, idx, visited)
            answer += 1
    return answer