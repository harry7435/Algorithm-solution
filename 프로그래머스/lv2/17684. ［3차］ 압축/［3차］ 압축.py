def solution(msg):
    answer = []
    index_list = {}
    max_index = 26                          # 현재 사전의 최대 인덱스
    # A~Z까지 기본 사전 만들기
    for i in range(26):
        index_list[chr(i+65)] = i+1
    # 현재 입력(w)과 새로운 문자(c)
    w = ''
    c = ''
    # LZW 압축 과정
    for idx in range(len(msg)):
        w += msg[idx]                       # 현재 입력에 현재 인덱스 문자 추가
        next_index = idx + 1                # 다음 인덱스 저장
        # 다음 인덱스가 범위 벗어나지 않을 때, 새로운 문자에 다음 인덱스 문자 추가
        if next_index < len(msg):
            c = w + msg[next_index]
            # 새로운 문자가 사전에 없을 경우
            if c not in index_list:
                answer.append(index_list[w])    # 현재 입력 출력
                max_index += 1                  # 사전 최대 인덱스 +1
                index_list[c] = max_index       # 새로운 문자 사전에 추가
                w = ''                          # 현재 입력 초기화
    # 마지막 처리되지 않은 현재 입력 출력
    answer.append(index_list[w])
    
    return answer