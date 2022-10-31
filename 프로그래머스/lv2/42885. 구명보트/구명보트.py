def solution(people, limit):
    answer = 0
    people.sort(reverse=True)  # 몸무게 많은 순으로 정렬
    big = 0
    small = len(people) - 1
    
    # 몸무게가 가장 큰 사람과 가장 작은 사람 합해서 제한에 안 걸리면
    # 둘 다 태우고, 아니면 큰 사람만 태운다
    while big <= small:
        if people[big] + people[small] <= limit:
            small -= 1
        big += 1
        answer += 1
    
    return answer