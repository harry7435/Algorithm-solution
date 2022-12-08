import sys
input = sys.stdin.readline

stack = []  # 괄호 스택
cal = 1     # 중간 계산 스택
answer = 0  # 쵱종 결과
s_list = list(input().rstrip())
# 괄호 체크 시작
for idx in range(len(s_list)):
    # "("일 경우
    if s_list[idx] == "(":
        # 스택에 추가 후 계산 스택 * 2
        stack.append(s_list[idx])
        cal *= 2
    # "["일 경우
    elif s_list[idx] == "[":
        # 스택에 추가 후 계산 스택 * 3
        stack.append(s_list[idx])
        cal *= 3
    # ")"일 경우
    elif s_list[idx] == ")":
        # 잘못된 괄호일 경우
        if not stack or stack[-1] == "[":
            # 정답 0 후 break
            answer = 0
            break
        # "()"이 매치됐을 경우
        if s_list[idx-1] == "(":
            # 현재 계산 스택을 answer에 더하기
            answer += cal
        # "()" 스택에서 제거
        stack.pop()
        # 계산 스택에 2를 나누기
        cal //= 2
    # "]"일 경우
    else:
        # 잘못된 괄호일 경우
        if not stack or stack[-1] == "(":
            # 정답 0 후 break
            answer = 0
            break
        # "[]"이 매치됐을 경우
        if s_list[idx-1] == "[":
            # 현재 계산 스택을 answer에 더하기
            answer += cal
        # "[]" 스택에서 제거
        stack.pop()
        # 계산 스택에 3을 나누기
        cal //= 3
# 스택이 남아 있을 경우 잘못된 괄호, answer = 0
if stack:
    answer = 0
print(answer)