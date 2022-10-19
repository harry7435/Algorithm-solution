def solution(n):
    answer = 0
    n_bin = bin(n)[2:]  # n의 이진 변환 
    while answer == 0:
        n += 1
        # n_bin의 1의 갯수와 n보다 큰 수의 이진 변환의 1의 갯수 비교
        if n_bin.count('1') == bin(n)[2:].count('1'):
            answer = n
    return answer