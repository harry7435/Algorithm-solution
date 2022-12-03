def solution(tickets):
    answer = []
    path = []
    stack = ['ICN']
    graph = {}
    # 그래프 만들기
    for ticket in tickets:
        dep, dis = ticket[0], ticket[1]
        if dep not in graph:
            graph[dep] = [dis]
        else:
            graph[dep].append(dis)
            # 알파벳 순서 반대로로 정렬
            graph[dep].sort(reverse=True)
    # dfs 스택 이용
    while stack:
        depart = stack[-1]
        # 티켓을 모두 다 소진한 경우
        if depart not in graph or len(graph[depart]) == 0:
            # 경로에 스택의 오른쪽부터 추출해서 추가
            path.append(stack.pop())
        # 그 외 스택에 티켓의 도착지점을 추가 후 티켓 제거
        else:
            stack.append(graph[depart].pop())
    # 경로가 거꾸로 되어있으므로 반전
    answer = path[::-1]
    return answer