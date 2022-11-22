from collections import deque

def bfs(start, tree, visited, wire, connect):
    queue = deque()
    queue.append([start, tree, visited, wire])
    visited[start] = True
    
    while queue:
        start, tree, visited, wire = queue.popleft()
        connect += 1
        
        for i in tree[start]:
            # 시작점과 추가할 지점이 전선 정보로 연결되지 않았을 때 queue에 추가
            if not ((start == wire[0] and i == wire[1]) or (start == wire[1] and i == wire[0])):
                if not visited[i]:
                    visited[i] = True
                    queue.append([i, tree, visited, wire])

    return connect

def solution(n, wires):
    answer = n
    tree = [[] for _ in range(n+1)]
    # 트리 생성
    for wire in wires:
        v1, v2 = wire
        tree[v1].append(v2)
        tree[v2].append(v1)
    # wire 하나씩 제거했을 때 분리된 송전탑 갯수 중 최솟값을 업데이트
    for wire in wires:
        visited = [False for _ in range(n+1)]
        temp = []
        for i in range(1, n+1):
            if not visited[i]:
                connect = bfs(i, tree, visited, wire, 0)
                temp.append(connect)
        # 최솟값 업데이트
        answer = min(answer, abs(temp[0] - temp[1]))
        
    return answer