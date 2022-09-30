from itertools import combinations as com

n, m = map(int, input().split())

pool = [str(i) for i in range(1, n+1)]

# 조합으로 만든 리스트 오름차순 정렬
list(com(pool, m)).sort()

for p in list(com(pool, m)):
  print(' '.join(list(p)))