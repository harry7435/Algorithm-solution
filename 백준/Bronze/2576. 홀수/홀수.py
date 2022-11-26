import sys
input = sys.stdin.readline
# 7개 자연수 입력
num_list = [int(input()) for _ in range(7)]
# 홀수의 합, 최소 홀수 구하기
num_sum = 0 
min_num = 100
for number in num_list:
    if number % 2 != 0:
        num_sum += number
        min_num = min(min_num, number)
# 홀수가 없으면 -1 출력
if num_sum == 0:
    print(-1)
else:
    print(num_sum)
    print(min_num)