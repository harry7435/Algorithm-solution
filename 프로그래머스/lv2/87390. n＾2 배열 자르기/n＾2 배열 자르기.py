def solution(n, left, right):
    answer = []
    # i행 = idx // n, j열 idx % n으로 치환가능
    # i행 j열을 숫자 i로 채우고 1차원으로 변형하여 추가하는 것을 한 번에 수행
    # left부터 right까지만 수행
    for idx in range(left, right+1):
        if idx // n >= idx % n:
            answer.append(idx // n + 1) 
        else: answer.append(idx % n + 1)
        
    return answer