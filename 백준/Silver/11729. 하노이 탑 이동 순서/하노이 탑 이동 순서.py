import sys
input = sys.stdin.readline
# n개의 원판을 출발지점(s)에서 끝지점(d)으로 옮기는 함수
def move_hanoi(n, s, d):
  if n == 1:
    print(s, d)
    
  else:
    # n-1개를 다른 곳에 옮겨 놓기
    # 여기서 끝지점은 1번 2번 3번 봉을 다 합치면 6이므로
    # 그 중 나머지를 택하면 6-s-d가 됨
    move_hanoi(n-1, s, 6-s-d)
  
    # 1개를 s에서 d로 옮기기
    print(s, d)
  
    # 다시 n-1을 옮기기
    move_hanoi(n-1, 6-s-d, d)

n = int(input())
print(2**n - 1) # 전체 옮기는 횟수
move_hanoi(n, 1, 3)