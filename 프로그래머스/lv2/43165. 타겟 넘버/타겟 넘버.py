from collections import deque

def solution(numbers, target):
    answer = 0
    queue = deque() # bfs를 위해 deque 사용
    length = len(numbers)
    # 첫 번째 값 queue에 추가, 인덱스와 함께 추가
    queue.append([numbers[0], 0])
    queue.append([-1 * numbers[0], 0])
    # 각 인덱스 다음 값에 더하고 빼기
    while queue:
        temp, idx = queue.popleft()
        idx += 1
        if idx < length:
            queue.append([temp+numbers[idx], idx])
            queue.append([temp-numbers[idx], idx])
        else:
            # 결과값이 타켓값과 같으면 answer에 추가
            if temp == target:
                answer += 1
    return answer