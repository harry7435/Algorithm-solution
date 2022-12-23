def solution(numbers):
    answer = ''
    numbers = list(map(str, numbers))   # 문자열로 치환
    # x * 3은 1000 이하 자연수이므로 세자리를 맞추기 위함, 내림차순 정렬
    numbers.sort(key=lambda x: x * 3, reverse=True)
    # 모든 값이 0일 수 있으므로 정수->문자열 변환 반복
    answer = str(int("".join(numbers)))
    return answer