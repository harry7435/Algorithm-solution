def solution(n, words):
    answer = []
    visited = []    # 끝말잇기 성공한 단어 리스트
    cnt = 0
    num = 0
    fail = True # 탈락자 유무 확인용
    for w in words:
        if w in visited:    # 이전에 동일한 단어가 있을 시 탈락
            fail = False
            
        if visited != []:   # 끝말잇기 조건 불만족 시 탈락
            if visited[-1][-1] != w[0]:
                fail = False
                
        visited.append(w)
        length = len(visited)
        if fail == False:   # 탈락 시 해당 단어의 번호와 차례 저장 후 반복문 종료
            num = length % n
            if num == 0: num = n
            cnt = (length - 1) // n + 1
            break
    answer = [num, cnt]

    return answer