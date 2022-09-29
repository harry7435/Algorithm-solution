n = int(input()) # 이동목표채널
m = int(input()) # 고장난 버튼 갯수
if m != 0: # 고장난 키가 있으면 입력받기
  error_b = input().split() 
else:
  error_b = []

edit_num = abs(100 - n) # 수정해야 하는 최대 채널수

# 999999에서부터 1까지 감소할 수도 있으므로 최댓값 1000000
for num in range(1000001):
  for i in str(num): # 숫자 문자열로 분할
    if i in error_b: # 고장난 키가 포함되어 있으면 건너뜀
      break
  # 고장난 키 포함 없이 만들 수 있으면 기존 최솟값과
  # 누를 키 갯수 + 누른 숫자와 목표 숫자와의 차이 중 작은 값 취하기
  else:
    edit_num = min(edit_num, len(str(num)) + abs(num-n))

print(edit_num)