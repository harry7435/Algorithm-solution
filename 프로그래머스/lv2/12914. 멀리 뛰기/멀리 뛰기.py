def solution(n):
    answer = 0
    dp = [0 for _ in range(2001)]
    dp[1] = 1
    dp[2] = 2
    for i in range(3, 2001):    # 피보나치 수열 점화식 성립 dp 구현하면 됨.
        dp[i] = dp[i-1] + dp[i-2]
    answer = dp[n] % 1234567
    
    return answer
