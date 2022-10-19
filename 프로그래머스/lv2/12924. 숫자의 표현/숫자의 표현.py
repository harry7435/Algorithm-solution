def solution(n):
    answer = 0
    for num in range(1, n+1):
        sum = 0
        for i in range(num, n+1):
            sum += i
            if sum > n: # 합이 n을 넘으면 불가능
                break
            elif sum == n:  # 연속한 숫자 합이 n이면 카운트 +1
                answer += 1
                break
    return answer