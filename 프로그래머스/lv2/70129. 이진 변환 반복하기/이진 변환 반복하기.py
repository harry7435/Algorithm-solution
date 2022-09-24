def make_two(x):
    list_x = list(x)
    count_0 = int(list_x.count('0'))
    change_x = bin(len(x) - count_0)[2:]
    return count_0, change_x
  
def solution(s):
    answer = []
    cnt = 0
    cnt_0 = 0
    while True:
        if s == '1':
            break
        c, s = make_two(s)
        cnt += 1
        cnt_0 += c
    
    answer = [cnt, cnt_0]
    return answer