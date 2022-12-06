import sys
input = sys.stdin.readline

t = int(input())
for i in range(t):
    # 배열 입력 후 정렬
    num_list = list(map(int, input().split()))
    num_list.sort()
    # 오른쪽에서 3번째 수 출력
    print(num_list[-3])