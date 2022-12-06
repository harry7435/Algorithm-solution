import sys
input = sys.stdin.readline

t = int(input())
# 이진수로 변환하면서 1이 나올 때마다 해당 idx 저장
for i in range(t):  
    n = int(input())
    idx = 0
    bin_num = []
    while n != 0:
        if n % 2 != 0:
            bin_num.append(str(idx))
        idx += 1
        n = n // 2
    # 공백 포함 출력
    print(" ".join(bin_num))