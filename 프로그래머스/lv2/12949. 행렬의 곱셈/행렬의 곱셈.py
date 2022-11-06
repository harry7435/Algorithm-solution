def solution(arr1, arr2):
    # arr2 형태 변환 (바로 곱하기 좋게)
    new_arr2 = []
    for i in range(len(arr2[0])):
        arr = []
        for a2 in arr2:
            arr.append(a2[i])
        new_arr2.append(arr)
    
    # 변형된 new_arr2와 arr1의 원소곱의 합을 저장
    answer = []
    for a1 in arr1:
        arr = []
        for a2 in new_arr2:
            multisum = 0
            for i in range(len(a1)):
                multisum += a1[i] * a2[i]
            arr.append(multisum)
        answer.append(arr)
        
    return answer