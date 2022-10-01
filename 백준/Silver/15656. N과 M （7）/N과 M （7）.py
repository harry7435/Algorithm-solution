from itertools import product as pro
# 중복순열 product 사용

n, m = map(int, input().split())

pool = list(map(int, input().split()))
pool.sort() # 수열을 사전 순으로 증가하는 순서로 정렬

# repeat 반복 횟수 = 수열 원소 갯수
for p in (pro(pool, repeat=m)):
  for num in p:
    print(num, end=' ')
  print('')