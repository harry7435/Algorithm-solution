def solution(s):
    answer = []
    # 갯수별 딕셔너리 생성
    num_dic = {}
    # 양쪽 {} 와 튜플들을 구분하기 위해 split하여 배열화
    s_list = s.strip("{}").split('},{')
    
    # 원소의 갯수를 key, 원소 배열을 value로 딕셔너리에 저장
    for i in s_list:
        num = len(i.split(","))
        num_dic[num] = i.split(",")
    
    # 원소 갯수 오름차순으로 중복되지 않게 순서대로 출력
    for k in range(1, len(s_list)+1):
        for n in num_dic[k]:
            if int(n) not in answer:
                answer.append(int(n))
        
    return answer