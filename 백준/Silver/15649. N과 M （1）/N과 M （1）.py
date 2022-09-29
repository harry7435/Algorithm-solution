from itertools import permutations as pe

n, m = map(int, input().split())

pool = [str(i) for i in range(1, n+1)] # 순열 만들 풀 만들기

for p in list(pe(pool, m)):
  print(' '.join(list(p))) # 공백 추가해서 출력