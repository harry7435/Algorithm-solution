from collections import deque

def solution(cacheSize, cities):
    answer = 0
    # 최대 캐시 크기만큼의 deque 생성
    cache = deque(maxlen = cacheSize)
    # 캐시 사이즈가 0이면 모든 도시 이름이 cache miss
    if cacheSize == 0:
        return len(cities) * 5

    for city in cities:
        city = city.lower() # 도시 이름 대소문자 모두 소문자로 통일
        if city in cache:
            answer += 1
            cache.remove(city)
            
        else:
            answer += 5
            
        cache.append(city)
    return answer