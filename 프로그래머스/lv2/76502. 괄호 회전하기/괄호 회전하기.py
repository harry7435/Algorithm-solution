def solution(s):
    # s의 길이가 홀수면 잘못된 괄호
    if len(s) % 2 != 0:
        return 0
    
    answer = 0
    for i in range(len(s)):
        new_s = s[i:] + s[:i]   # 0~s만큼 회전하여 체크
        stack = []
        for n in new_s:
            # ], }, ) 일 경우 최근 stack이 존재하며 [, {, ( 로 닫힐 경우 pop
            if n == "]":
                if stack != []:
                    if stack[-1] == "[":
                        stack.pop()
                else:
                    stack.append(n)
            elif n == "}":
                if stack != []:
                    if stack[-1] == "{":
                        stack.pop()
                else:
                    stack.append(n)
            elif n == ")":
                if stack != []:
                    if stack[-1] == "(":
                        stack.pop()
                else:
                    stack.append(n)
            else:
                stack.append(n)
        
        # 마지막에 스택이 남아있지 않다면 올바른 괄호
        if stack == []:
            answer += 1
    return answer