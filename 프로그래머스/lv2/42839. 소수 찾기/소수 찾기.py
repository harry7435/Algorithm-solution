from itertools import permutations
# 소수 판별 함수
def is_prime(x):
    if x <= 1:
        return False
    for i in range(2, int(x ** 0.5)+1):
        if x % i == 0:
            return False
    return True

def solution(numbers):
    answer = 0
    num_list = list(numbers)
    check = []
    # 가능한 숫자 조합 구하기
    for i in range(1, len(numbers)+1):
        perm = set(map(''.join, permutations(numbers, i)))
        for p in perm:
            # 소수이면서 체크 안 된 경우, 추가 후 갯수 +1
            if int(p) not in check and is_prime(int(p)):
                check.append(int(p))
                answer += 1
    return answer