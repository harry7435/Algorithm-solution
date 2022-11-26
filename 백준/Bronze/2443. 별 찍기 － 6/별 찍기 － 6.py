import sys
input = sys.stdin.readline

n = int(input())

for row in range(n):
    space = " " * row       # 양쪽 공백
    star = "*" * (2 * (n-row) -1)  # 별 갯수
    # 줄바꿈 제외 후 출력
    if row == n-1:
        print(space + star, end="")
    else:
        print(space + star)