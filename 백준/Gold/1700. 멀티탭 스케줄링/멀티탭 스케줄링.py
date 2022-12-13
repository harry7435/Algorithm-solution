import sys
input = sys.stdin.readline

n, k = map(int, input().split())
numbers = list(map(int, input().split()))
plug = []
off = 0
# 사용 순서대로 진행
for idx in range(k):
    # 이미 플러그에 있는 용품일 경우
    if numbers[idx] in plug:
        continue
    # 플러그가 꽉 차 있지 않을 경우
    if len(plug) < n:
        plug.append(numbers[idx])
        continue
    # 이후 용품 사용 순서
    use_order = []
    left_number = numbers[idx:]
    all_plug_will_use = True
    # 플러그에 모든 용품이 이후 사용되는지 체크
    for i in range(n):
        if plug[i] in left_number:
            use_order.append(left_number.index(plug[i]))
        else:
            use_order.append(1000)
            all_plug_will_use = False
        # 하나라도 사용 안되면 break
        if not all_plug_will_use: break
    # 가장 나중에 사용되는 용품 제거
    last_use = use_order.index(max(use_order))
    plug.pop(last_use)
    # 용품 추가
    plug.append(numbers[idx])
    off += 1

print(off)