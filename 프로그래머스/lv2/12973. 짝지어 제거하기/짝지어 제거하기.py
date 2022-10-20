def solution(s):
    answer = -1
    stack = []
    for i in s:
        if stack == []:  # 처음에는 stack에 추가
            stack.append(i)
        elif stack[-1] == i:    # 이전 stack 요소가 연속되면 pop으로 제거
            stack.pop()
        else:   # 연속이 아니면 stack에 추가
            stack.append(i)
    # 빈 stack이면 짝맞춰 삭제 가능
    if not stack: answer = 1
    else: answer = 0
    return answer