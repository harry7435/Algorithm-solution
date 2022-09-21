import sys
input = sys.stdin.readline
cnt = 0

def recursion(s, l, r):
    global cnt  # 전역변수 cnt 설정
    cnt += 1    # 실행 될 때마다 횟수 세기
    if l >= r: return 1
    elif s[l] != s[r]: return 0
    else: return recursion(s, l+1, r-1)

def isPalindrome(s):
    return recursion(s, 0, len(s)-1)

t = int(input())

for i in range(t):
  s = input().rstrip()
  cnt = 0  # 횟수 초기화하기
  is_pal = isPalindrome(s)
  print(is_pal, cnt)