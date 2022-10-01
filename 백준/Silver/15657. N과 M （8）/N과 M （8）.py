from itertools import combinations_with_replacement as cwr
# 중복조합 combinations_with_replacement 사용

n, m = map(int, input().split())

pool = list(map(int, input().split()))
pool.sort() # 수열을 사전 순으로 증가하는 순서로 정렬

for p in (cwr(pool, m)):
  for num in p:
    print(num, end=' ')
  print('')