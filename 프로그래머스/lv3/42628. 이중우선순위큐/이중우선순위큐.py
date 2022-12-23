import heapq
def solution(operations):
    answer = []
    min_heap = []
    max_heap = []
    for operation in operations:
        do, num = operation.split()
        # 큐에 숫자 추가
        if do == "I":
            num = int(num)
            heapq.heappush(min_heap, num)
            heapq.heappush(max_heap, (-num, num))
        else:
            # 큐가 비었을 경우 무시
            if len(min_heap) == 0:
                pass
            # 최댓값 삭제
            elif num == "1":
                max_num = heapq.heappop(max_heap)[1]
                min_heap.remove(max_num)
            # 최솟값 삭제
            elif num == "-1":
                min_num = heapq.heappop(min_heap)
                max_heap.remove((-min_num, min_num))
    # 큐가 비어있지 않을 경우
    if min_heap:
        answer = [heapq.heappop(max_heap)[1], heapq.heappop(min_heap)]
    else:
        answer = [0, 0]
    return answer