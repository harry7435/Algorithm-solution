import sys
input = sys.stdin.readline

n, k = map(int, input().split())
div_list = []
# 약수 리스트 구하기
for i in range(1, n+1):
    if n % i == 0:
        div_list.append(i)
# 약수 갯수가 k보다 작으면 0 출력
if len(div_list) < k:
    print(0)
else:
    print(div_list[k-1])