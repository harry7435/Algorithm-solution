import heapq # 힙큐 사용
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville) # 기존 리스트 힙큐화
    # 최소 스코빌 지수가 K보다 작을 때만 실행
    while scoville[0] < K:
        try:
            # 가장 작은 스코빌 지수와 그 다음으로 작은 스코빌 지수 추출
            s1 = heapq.heappop(scoville)
            s2 = heapq.heappop(scoville)
            # 새로운 음식 스코빌 지수 힙큐에 추가
            heapq.heappush(scoville, s1 + s2 * 2)
        # 수행 불가능의 경우 -1 리턴
        except IndexError:
            return -1
        # 섞은 횟수 +1
        answer += 1
    return answer