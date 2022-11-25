def solution(record):
    answer = []
    user = {}   # 유저 아이디, 닉네임 정보
    # 최종 유저 아이디와 닉네임 구하기
    for rec in record:
        rec = rec.split(" ")
        # Enter or Change
        if len(rec) == 3:
            user[rec[1]] = rec[2]
    # 결과 출력
    for rec in record:
        rec = rec.split(" ")
        # 들어왔을 때
        if rec[0] == 'Enter':
            answer.append(f"{user[rec[1]]}님이 들어왔습니다.")
        # 나갔을 때
        elif rec[0] == 'Leave':
            answer.append(f"{user[rec[1]]}님이 나갔습니다.")
    return answer