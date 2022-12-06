import sys
input = sys.stdin.readline

start, end = map(int, input().split())
arr = []
idx = 0
# 최대 1000개까지 배열을 구하기
while len(arr) < 1000:
    idx += 1
    for i in range(idx):
        arr.append(idx)
arr = arr[:1000]
# 구간 내 합 출력
print(sum(arr[start-1:end]))