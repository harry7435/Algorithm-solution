def solution(n):
    answer = 0
    dp = [0 for _ in range(100001)]
    dp[0] = 0
    dp[1] = 1
    for num in range(2, n+1):   # 피보나치 수열 규칙에 따라 다음 dp 구하기
        dp[num] = dp[num-1] + dp[num-2]
    
    answer = dp[n] % 1234567
    return answer