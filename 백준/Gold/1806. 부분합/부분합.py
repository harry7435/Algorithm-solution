import sys
input = sys.stdin.readline

n, s = map(int, input().split())
numbers = list(map(int, input().split()))
min_length = n+1
start, end = 0, 0   # 투 포인터 설정
sum_temp = 0
# 시작점이 배열의 끝이 될 때까지 수행
while True:
    # 배열의 합이 s 이상일 경우
    if sum_temp >= s:
        min_length = min(min_length, end - start)   # 최소 길이 저장
        sum_temp -= numbers[start]  # 시작점 배열 값 빼기
        start += 1  # 시작점 +1
    # 끝점이 배열의 끝이면 중단
    elif end == n:
        break
    # 배열의 합이 s 이하일 경우
    else:
        sum_temp += numbers[end]    # 끝점 배열 값 더하기
        end += 1    # 끝점 +1
# 만족하는 경우가 없는 경우 0 출력
if min_length == n+1:
    print(0)
else:
    print(min_length)