# 소수 체크
def check_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
# k 진법으로 변환
def change_k(num, k):
    answer = []
    while num != 0:
        answer.append(num % k)
        num = num // k
    answer.reverse()
    return answer

def solution(n, k):
    answer = 0
    change_num = change_k(n, k)
    # 0을 기준으로 숫자 슬라이싱
    num_list = []
    temp = ''
    for c in change_num:
        if c == 0:
            num_list.append(temp)
            temp = ''
        else:
            temp += str(c)
    num_list.append(temp)
    # 소수 갯수 구하기
    for num in num_list:
        if num != '' and check_prime(int(num)):
            answer += 1
    return answer