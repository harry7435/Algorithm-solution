def solution(name):
    answer = 0
    joystick_num = []   # 위아래 조이스틱 횟수 리스트
    # N(78) 기준으로 최소 조작 횟수(위아래) 저장
    for n in name:
        if int(ord(n)) <= 78:
            joystick_num.append(int(ord(n)) - 65)
        else:
            joystick_num.append(91 - int(ord(n)))
    min_move = len(name) - 1    # 초기 최소 이동거리는 알파벳 길이 - 1
    # 연속 A 기준으로 앞 뒤 최소 이동거리 구하기
    for i in range(len(joystick_num)):
        end = i+1
        while end < len(name) and name[end] == 'A':
            end += 1
        min_move = min(min_move, 2 * i + len(name) - end, 2 * (len(name) - end) + i)
    
    answer = sum(joystick_num) + min_move
    return answer
