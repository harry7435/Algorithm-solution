def solution(clothes):
    answer = 1
    clothes_dic = {}
    
    # 의상의 종류를 key, 갯수를 value로 가지는 딕셔너리 생성
    for c in clothes:
        if c[1] in clothes_dic:
            clothes_dic[c[1]] += 1
        else:
            clothes_dic[c[1]] = 1
    
    # 각 의상 종류의 갯수로 이루어진 조합을 계산
    for d in list(clothes_dic.values()):
        answer *= (d+1)
    answer -= 1
    return answer