import sys
input = sys.stdin.readline

train = 0
max_train = 0
# 각 역에서 (탄 사람 - 내린 사람)을 전체 사람 수에 더함
for i in range(10):
    off, on = map(int, input().split())
    train = train + on - off
    # 최댓값과 비교해서 크면 최댓값 갱신
    max_train = max(max_train, train)
# 최댓값 출력
print(max_train)