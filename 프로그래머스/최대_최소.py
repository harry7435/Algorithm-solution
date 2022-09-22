def solution(s):
  answer = ''
  s_split = list(map(int, s.split()))
  s_split.sort()
  m = s_split[-1]
  n = s_split[0]
  answer = str(n) + ' ' + str(m)
  return answer