from collections import deque

def solution(n, edge):
    answer = 0
    graph = [[] for _ in range(n+1)]
    # vertext graph 생성
    for e in edge:
        a, b = map(int, e)
        graph[a].append(b)
        graph[b].append(a)
    # bfs
    # 큐, 방문배열 생성
    queue = deque()
    queue.append(1)
    visited = [0 for _ in range(n+1)]
    visited[1] = 1
    # bfs 수행
    while queue:
        nodes = queue.popleft()
        # 방문하지 않은 노드일 경우 이전 노드 + 1 갱신
        for next_node in graph[nodes]:
            if visited[next_node] == 0:
                visited[next_node] = visited[nodes]+1
                queue.append(next_node)
    # 최댓값 추출
    max_level = max(visited)
    cnt_max = visited.count(max_level)
    # 최댓값이 0보다 클 때
    if cnt_max > 0: answer = cnt_max
    else: answer = 1
                
    return answer