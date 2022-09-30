from itertools import permutations as per
# 순열 사용

n, m = map(int, input().split())

pool = list(map(int, input().split()))


for p in sorted(per(pool, m)):
  for num in p:
    print(num, end=' ')
  print('')