from itertools import product as pu

n, m = map(int, input().split())

pool = [str(i) for i in range(1, n+1)]

# 중복가능한 순열로 만든 리스트 오름차순 정렬
list(pu(pool, repeat=m)).sort() # product 사용, repeat은 중복 사용 가능 횟수

for p in list(pu(pool, repeat=m)):
  print(' '.join(list(p)))