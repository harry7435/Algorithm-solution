n, m, k = map(int, input().split())
board_list = []
for i in range(n):
  board_list.append(list(map(int, input().split())))
# 방문체크용
visited = [[False]*m for i in range(n)]
# 인접 좌표 체크
move = [(1, 0), (0, 1), (-1, 0), (0, -1)]
# 최솟값 초기 설정
max_sum = -1000000

def dfs(x, y, cnt, temp_sum):
  # k개 시도 후 더한 값
  if cnt == k:
    global max_sum
    if temp_sum > max_sum:
      max_sum = temp_sum
    return

  for i in range(x, n):
    for j in range(y if i == x else 0, m):
      # 이전에 방문했는지 확인
      if visited[i][j]:
        continue
      # 인접한 곳 방문했는지 확인
      check = True
      for t in range(4):
        x_t = i + move[t][0]
        y_t = j + move[t][1]
        if 0 <= x_t < n and 0 <= y_t < m:
          if visited[x_t][y_t]:
            check = False
      # 인접한 곳 방문 안했을 때 합계에 값 추가
      if check:
        visited[i][j] = True
        dfs(i, j, cnt+1, temp_sum+board_list[i][j])
        visited[i][j] = False

dfs(0, 0, 0, 0)

print(max_sum)