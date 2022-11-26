import sys
input = sys.stdin.readline

n = int(input())
# 위쪽 부분
for row in range(1, n):
    space = " " * (n-row)     # 양쪽 공백
    star = "*" * (2 * row -1)  # 별 갯수
    # 별 출력
    print(space + star)
# 아래 부분
for row in range(n):
    space = " " * row    # 양쪽 공백
    star = "*" * (2 * (n-row) -1)  # 별 갯수
    # 별 출력
    if row == n-1:
        print(space + star, end="")
    else:
        print(space + star)