def solution(brown, yellow):
    answer = []
    max_value = brown + yellow
    for h in range(1, int(max_value ** 0.5)+1):
        # 조건1) 가로 * 세로 = brown * yellow 이어야 함
        if max_value % h == 0:
            w = max_value // h
            # 조건 2) 가로 + 세로 - 2 = brown / 2 이어야 함
            if h + w - 2 == brown // 2:
                answer = [w, h]
            # 적정값 찾으면 종료
            if answer != []:
                break
    return answer