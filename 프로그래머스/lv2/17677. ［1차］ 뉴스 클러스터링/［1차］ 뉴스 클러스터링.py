def solution(str1, str2):
    answer = 0
    # 문자를 소문자로 간소화
    str1 = str1.lower()
    str2 = str2.lower()
    # 연속한 두 문자가 둘 다 소영문자일 경우만 다중문자 리스트에 추가
    multi1 = []
    multi2 = []
    for i in range(len(str1)-1):
        if 97 <= ord(str1[i]) <= 122 and 97 <= ord(str1[i+1]) <= 122:
            multi1.append(str1[i] + str1[i+1])
    
    for i in range(len(str2)-1):
        if 97 <= ord(str2[i]) <= 122 and 97 <= ord(str2[i+1]) <= 122:
            multi2.append(str2[i] + str2[i+1])
            
    multi2_copy = multi2.copy() # multi2 원본 유지 위해 copy
    inter = 0
    uni = 0
    # 교집합과 합집합 구하기
    for m1 in multi1:
        if m1 in multi2_copy:
            inter += 1
            uni += 1
            multi2_copy.remove(m1)
        else:
            uni += 1
    uni += len(multi2_copy)
    # zero division 방지
    if uni == 0:
        answer = 65536
    else:
        answer = int(inter / uni * 65536)
    return answer