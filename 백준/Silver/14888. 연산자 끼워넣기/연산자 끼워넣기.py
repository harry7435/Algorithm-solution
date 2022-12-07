import sys
input = sys.stdin.readline
# 재귀 dfs 사용
def dfs(plus, minus, multi, divide, level, answer):
    global min_num, max_num
    # n개 숫자의 연산이 끝나면 최댓값, 최솟값 return
    if level == n:
        min_num = min(min_num, answer)
        max_num = max(max_num, answer)
        return
    # 각 연산이 남아 있으면 수행
    if plus != 0:
        dfs(plus-1, minus, multi, divide, level+1, answer+number_list[level])
    if minus != 0:
        dfs(plus, minus-1, multi, divide, level+1, answer-number_list[level])
    if multi != 0:
        dfs(plus, minus, multi-1, divide, level+1, answer*number_list[level])
    if divide != 0:
        dfs(plus, minus, multi, divide-1, level+1, int(answer / number_list[level]))

n = int(input())
number_list = list(map(int, input().split()))
plus, minus, multi, divide = map(int, input().split())
# 초기 최대, 최소 설정
min_num, max_num = 1e9, -1e9
level = 1
# 재귀 수행
dfs(plus, minus, multi, divide, level, number_list[0])
# 출력
print(max_num)
print(min_num)