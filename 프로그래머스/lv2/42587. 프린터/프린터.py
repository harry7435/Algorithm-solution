def solution(priorities, location):
    answer = 0
    while True:
        max_priorities = max(priorities)            # 현재 최대 중요도 저장
        check = priorities.pop(0)               # 가장 앞에 있는 문서 J 꺼내기
        
        # 최대 중요도일 경우
        if max_priorities == check:
            answer += 1                         # 인쇄 횟수 + 1
            
            # 출력된 값이 원하는 location 값일 경우 중단
            if location == 0:
                break
            else:
                location -= 1
        else:
            priorities.append(check)            # 최대값이 아닐 경우 맨 뒤로 보내기
            
            # 하나씩 location이 당겨짐
            if location == 0:
                location = len(priorities) - 1
            else:
                location -= 1
    return answer