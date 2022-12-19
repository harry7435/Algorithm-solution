import heapq

def solution(jobs):
    answer = 0
    current_time, success_job, start_time = 0, 0 ,-1
    job_heap = []
    
    while success_job < len(jobs):
        # 현재 시간에 요청한 작업이 있는 경우 힙에 추가
        for job in jobs:
            request_time, time_take = job[0], job[1]
            if start_time < request_time <= current_time:
                # 시간이 적게 걸리는 순으로 정렬하기 위해 역순으로 힙에 추가
                heapq.heappush(job_heap, [time_take, request_time])
        # 처리할 작업 힙이 있는 경우
        if len(job_heap) > 0:
            current_job = heapq.heappop(job_heap)
            start_time = current_time   # 실제 작업 시작 시간 갱신
            current_time += current_job[0]
            # 작업 종료시간 - 요청 시점 시간 =  소요시간
            answer += current_time - current_job[1]
            success_job += 1 # 완료 작업 수 +1
        else:
            current_time += 1 # 1초 후 탐색
    # 평균 구하기
    answer = answer // len(jobs)
    return answer