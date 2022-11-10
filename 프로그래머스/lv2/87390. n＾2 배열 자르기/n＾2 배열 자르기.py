def solution(n, left, right):
    answer = []
    arr = []
    # i행(n * i) j열을 숫자 i로 채우고 1차원으로 변형하는 것을 한 번에 수행
    # for i in range(n):
    #     for j in range(n):
    #         if i >= j:
    #             arr[n * i + j] = i + 1  # n * i + j로 변환
    #         else: arr[n * i + j] = j + 1
            
    # i행 = idx // n, j열 idx % n으로 치환가능
    # i행 j열을 숫자 i로 채우고 1차원으로 변형하는 것을 한 번에 수행
    # left부터 right까지만 수행
    for idx in range(left, right+1):
        if idx // n >= idx % n:
            arr.append(idx // n + 1) 
        else: arr.append(idx % n + 1)
        
    answer = arr
    return answer