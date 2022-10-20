N = int(input())
S = [list(map(int, input().split())) for i in range(N)]
visited = [False for _ in range(N)]

MIN_SCORE = 100000

def get_min(start, cnt):
  global S, MIN_SCORE
  
  # 팀을 다 나누면 각 팀 스탯 더하기
  if cnt == N / 2:
    start_team,  link_team = 0, 0
    for i in range(N):
      for j in range(N):
        if visited[i] and visited[j]: # 둘 다 True면 start팀
          start_team += S[i][j]
        elif not visited[i] and not visited[j]: # 둘 다 False면 link팀
          link_team += S[i][j]
    # 두 팀 간 스탯 차이가 MIN_SCORE보다 작으면 치환
    MIN_SCORE = min(MIN_SCORE, abs(start_team - link_team))
    return

  # 팀 수 나누기
  for i in range(start, N):
    if not visited[i]:
      visited[i] = True
      get_min(i+1, cnt+1)
      visited[i] = False

get_min(0, 0)
print(MIN_SCORE)