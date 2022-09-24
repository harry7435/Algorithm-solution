def solution(s):
    answer = list(s.title())
    for i in range(len(answer)):
      if answer[i] in '0123456789':
        if i+1 != len(answer):
          answer[i+1] = answer[i+1].lower()
    answer = ''.join(answer)
    return answer