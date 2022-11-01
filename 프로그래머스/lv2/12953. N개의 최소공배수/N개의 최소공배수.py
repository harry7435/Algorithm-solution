def get_gcd(a, b):  # 최대공약수 구하는 함수
    a, b = min(a, b), max(a, b)
    if a == 0:
        return b
    if b % a == 0:
        return a
    else: return get_gcd(a, b%a)

def solution(arr):
    answer = 0
    new_arr = []
    for i in range(len(arr)):   # 배열 중 서로의 약수가 되는 수 제거
        is_div = False
        for a in arr[i+1:]:
            if a % arr[i] == 0:
                is_div = True
        
        if not is_div:
            new_arr.append(arr[i])
    
    answer = new_arr[0] # 처음 값 대입
    for a in new_arr:   # 서로의 최소공배수 누적해서 구하기
        answer = int(answer * a / get_gcd(answer, a))
        
    return answer