from itertools import combinations_with_replacement  as comre

n, m = map(int, input().split())

pool = [str(i) for i in range(1, n+1)]

# 중복가능한 순열로 만든 리스트 오름차순 정렬
list(comre(pool, m)).sort() # 중복조합 combinations_with_replacement 사용

for p in list(comre(pool, m)):
  print(' '.join(list(p)))