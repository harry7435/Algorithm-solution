def solution(progresses, speeds):
    answer = []
    work = []                   # 작업 완료까지 필요한 일수 리스트
    num_work = len(progresses)  # 작업 갯수
    
    # 남은 진도율에 작업 속도를 나눠 남은 작업 일수를 구함
    for idx in range(num_work):
        left = 100 - progresses[idx]
        if left % speeds[idx] != 0:
            left_day = left // speeds[idx] + 1
        else:
            left_day = left // speeds[idx]
        work.append(left_day)
    
    stack = work[0]             # 앞서 기다려야하는 최대 작업 일수
    distribute = 0              # 배포 시 작업 갯수
    
    for day in work:
        # 남은 작업 일수가 최대 작업 일수보다 작거나 같으면 배포 대기 작업 수 추가
        if day <= stack:
            distribute += 1
        # 크면 이전까지 대기하고 있던 작업 배포 후 다시 1개부터 시작
        else:
            stack = day         # 최대 작업 대기 일수에 추가
            answer.append(distribute)
            distribute = 1
            
    answer.append(distribute)   # 마지막 남은 배포 갯수 추가
    return answer