import sys
input = sys.stdin.readline

t = int(input())    # 테스트 케이스
for i in range(t):
    n, m= map(int, input().split())
    # 문서 중요도
    queue = list(map(int, input().split()))
    goal = 0    # 뽑히는 순서
    while queue:
        max_value = max(queue)  # 현재 중요도 최댓값
        check = queue.pop(0)    # 현재 맨 처음 값
        m -= 1                  # 인덱스 하나씩 당겨짐
        # 처음 값이 최댓값이 아닐 때
        if check < max_value:
            queue.append(check) # 다시 맨 뒤에 추가
            # 처음 값이 목표 문서면 가장 마지막 인덱스로 복원
            if m == -1:
                m = len(queue) - 1
        # 최댓값일 때
        else:
            # 인쇄 후 뽑히는 순서 +1
            goal += 1
            # 인쇄된 것이 목표 문서면 출력
            if m == -1:
                print(goal)
                break