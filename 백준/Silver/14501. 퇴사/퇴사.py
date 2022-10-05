import sys
input = sys.stdin.readline

n = int(input())
# 거꾸로 연산하기 위해 dp[n+1]까지 만듬
dp = [0 for _ in range(n+2)]
talk = [[0,0]] # 인덱스 맞추기 위해 0번째 리스트 추가
for i in range(n):
  talk.append(list(map(int, input().split())))
# 마지막 날짜부터 최댓값 연산
for i in range(n, -1, -1):
  # 날짜와 t를 더한 값이 퇴사날을 넘으면 이전 dp값
  if talk[i][0] + i > n+1:
    dp[i] = dp[i+1]
  # 이전 dp값, 해당 날짜 상담 비용 + 상담 끝나는 날 dp값 중 큰 값
  else:
    dp[i] = max(dp[i+1], dp[i+talk[i][0]] + talk[i][1])

print(dp[0])