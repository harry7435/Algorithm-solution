def solution(s):
    answer = True
    stack = []
    for i in s:
        # '('는 그냥 스택에 추가
        if i == '(':
            stack.append(i)
        else:
            # 스택의 마지막이 '('일 때 ')'를 추가하면 '()' 한 쌍 삭제
            if stack != [] and stack[-1] == '(':
                stack.pop()
            # 그 이외에는 ')' 스택에 추가
            else:
                stack.append(i)
    # 스택이 모두 소진되면 올바른 괄호
    if stack: answer = False
    return answer