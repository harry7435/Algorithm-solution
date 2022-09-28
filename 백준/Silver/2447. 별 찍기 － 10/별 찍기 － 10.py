n = int(input())
board = [[' ' for i in range(n)] for i in range(n)]

def star(x):
  global board
  
  # 단위 별 구성 만들기
  if x == 3:
    board[0][:3] = ['*', '*', '*']
    board[1][:3] = ['*', ' ', '*']
    board[2][:3] = ['*', '*', '*']
    return

  row_x = x // 3 # 단위 별 구성까지 재귀해 들어가기
  star(row_x)
  
  # 단위 별 구성을 기준으로 빈 board를 채워 나가기
  for i in range(3):
    for j in range(3):
      if i == 1 & j == 1:
        continue
      for k in range(row_x):
        board[row_x * i + k][row_x * j : row_x * (j+1)] = board[k][:row_x]

star(n) # 함수 실행

for line_board in board:
  print(''.join(line_board)) 