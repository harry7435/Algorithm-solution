import sys
input = sys.stdin.readline
import heapq

t = int(input())
for i in range(t):
    heap = []
    # 중앙값 기준 최대힙, 최소힙 생성
    upper_median = []
    lower_median = []
    # 정수 입력
    m = int(input())
    number_list = list(map(int, input().split()))
    for row in range(m // 10):
        number_list += list(map(int, input().split()))
    # 초기 중앙값 설정
    median = number_list[0]
    median_list = [median]
    # 중앙값 리스트 만들기
    for i in range(1, m):
        number = number_list[i]
        # 중앙값보다 크면 최대힙에 추가
        if number > median:
            heapq.heappush(upper_median, number)
        # 작거나 같으면 최소힙에 추가
        else:
            heapq.heappush(lower_median, (-number, number))
        # 홀수번째 수
        if i % 2 == 0:
            # 최대힙이 최소힙보다 원소 갯수가 많으면
            if len(upper_median) > len(lower_median):
                # 최소힙에 현재 중앙값 추가
                # 최대힙에서 최솟값을 중앙값으로 지정
                heapq.heappush(lower_median, (-median, median))
                median = heapq.heappop(upper_median)
            # 최소힙이 최대힙보다 원소 갯수가 많으면
            elif len(upper_median) < len(lower_median):
                # 최대힙에 현재 중앙값 추가
                # 최소힙에서 최솟값을 중앙값으로 지정
                heapq.heappush(upper_median, median)
                median = heapq.heappop(lower_median)[1]
            # 수정된 중앙값을 리스트에 추가
            median_list.append(median)
    # 중앙값 갯수 및 중앙값 원소 출력
    print(len(median_list))
    print(" ".join(list(map(str,(median_list)))))