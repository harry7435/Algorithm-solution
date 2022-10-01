from itertools import combinations as com
# 순열 사용

n, m = map(int, input().split())

pool = list(map(int, input().split()))
pool.sort()

for p in (com(pool, m)):
  for num in p:
    print(num, end=' ')
  print('')