from collections import deque
# 최소 단계이므로 최단거리 bfs 사용
def solution(begin, target, words):
    answer = 0
    visited = [0 for _ in range(len(words))]
    queue = deque()
    queue.append([begin, 0])    # 초기 단어와 0단계 큐에 추가
    # bfs 수행
    while queue:
        word, level = queue.popleft()   # 현재 단어 추출
        # 타겟 단어와 같으면 현재 단계 출력
        if word == target:
            answer = level
            return answer
        # 다르면 비교
        else:
            for i in range(len(words)):
                diff = 0
                # 방문하지 않은 단어일 경우
                if visited[i] == 0:
                    # 하나만 다를 경우 큐에 추가
                    for w in range(len(word)):
                        if word[w] != words[i][w]:
                            diff += 1
                    if diff == 1:
                        queue.append([words[i], level+1])
                        visited[i] = 1
    return answer