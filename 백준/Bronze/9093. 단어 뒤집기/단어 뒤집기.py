import sys
input = sys.stdin.readline

t = int(input())
for i in range(t):
    # 문장 입력 후, 띄어쓰기 기준 분리
    sentence = input().rstrip().split(" ")
    # 단어를 뒤집어 새로운 문장 만들기
    new_sentence = []
    for word in sentence:
        new_sentence.append(word[::-1])
    # 공백 포함해서 출력
    print(' '.join(new_sentence))