def get_next_number(x): # 다음 번호 부여 함수
    if x % 2 == 0:
        return x//2
    else: return (x+1) // 2

def solution(n,a,b):
    answer = 0
    while abs(a-b) != 0:    # 같은 다음 번호를 부여 받으면 해당 라운드에서 붙은 것
        answer += 1
        a = get_next_number(a)
        b = get_next_number(b)
    return answer