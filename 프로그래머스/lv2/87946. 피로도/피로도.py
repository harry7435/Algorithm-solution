from itertools import permutations

def solution(k, dungeons):
    answer = []
    # 던전 갯수만큼 가능한 던전 탐험 순서 순열 생성
    idx = [x for x in range(len(dungeons))]
    dungeons_list = list(permutations(idx))
    # 각 경우마다 탐험 횟수 구하기
    for dungeon in dungeons_list:
        life = k
        explore = 0
        for i in dungeon:
            if life >= dungeons[i][0]:
                explore += 1
                life -= dungeons[i][1]
        answer.append(explore)
    # 최대 탐험 횟수 출력
    return max(answer)