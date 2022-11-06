def solution(citations):
    answer = -1
    citations.sort(reverse=True)    # 내림차순으로 정렬 6 5 3 1 0
    for i in range(len(citations)):
        # 인용 횟수가 인덱스보다 작거나 같아질 때 인덱스가 최댓값
        if citations[i] <= i:
            answer = i
            break
    # 인용 횟수가 모두 같으면 논문 갯수가 h-index
    if answer == -1:
        answer = len(citations)
    return answer