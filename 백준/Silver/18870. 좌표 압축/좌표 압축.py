import sys
input = sys.stdin.readline

n = int(input())
x = list(map(int, input().split()))
x_set = list(set(x))
x_set.sort()

dic = {}
for i in range(len(x_set)):
  dic[x_set[i]] = str(i)

ans = []
for a in x:
  ans.append(dic[a])

print(' '.join(ans))