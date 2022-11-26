def solution(prices):
    answer = []
    check_down = []
    num = len(prices)
    # 주식가격 비교
    for idx in range(num):
        standard = prices[idx]  # 기준가격
        is_ok = True            # 끝까지 가격이 떨어지지 않는지 확인
        # 기준가격과 이후 가격 비교
        for j in range(idx+1, num):
            # 기준가격보다 이후 가격이 작아지는 시점
            if standard > prices[j]:
                answer.append(j-idx)    # 해당 인덱스 - 기준가격 인덱스 입력
                is_ok = False           # 가격 유지 불가
                break
        # 끝까지 가격 유지됐을 경우 : 최대 인덱스 - 기준가격 인덱스
        if is_ok: answer.append(num-idx-1)
    return answer