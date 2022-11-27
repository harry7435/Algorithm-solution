def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = [0 for _ in range(bridge_length)]  # 다리 생성
    # 모두 다 다리를 지날 때까지 수행                                  
    while bridge:
        bridge.pop(0) # 다리 맨 왼쪽부터 하나씩 빼내기
        # 대기 트럭이 존재하며
        if truck_weights != []:
            # 다리 무게 한계를 넘지 않을 때
            if sum(bridge) + truck_weights[0] <= weight:
                # 다리에 트럭 추가
                bridge.append(truck_weights.pop(0))
            # 그 외 다리에 추가하지 않음(0 추가)
            else:
                bridge.append(0)
        # 매 작업마다 1초씩 소요
        answer += 1
    return answer