import sys
input = sys.stdin.readline

n, k = map(int, input().split())
word_learn = [0] * 26
word_list = [set(input().rstrip()) for _ in range(n)]
answer = 0
# 남극언어 접두, 접미어는 미리 읽을 줄 알아야 함
for w in ['a', 'n', 't', 'i', 'c']:
    word_learn[ord(w) - 97] = 1
# dfs 재귀 사용
def dfs(word_ord, limit):
    global answer
    # 가르치는 최대 단어 수 도달 시
    if limit == k-5:
        read_word = 0
        # 단어 리스트 중 읽을 수 있는 단어 수 체크
        for word in word_list:
            can_read = True
            for w in word:
                if word_learn[ord(w) - 97] == 0:
                    can_read = False
                    break
            if can_read:
                read_word += 1
        # 최댓값 갱신
        answer = max(answer, read_word)
        return
    # 제한된 갯수만큼 단어를 선택하는 모든 경우의 수 재귀
    for i in range(word_ord, 26):
        if word_learn[i] == 0:
            word_learn[i] = 1
            dfs(i, limit+1)
            word_learn[i] = 0
# k가 5개 미만일 경우 어떤 단어도 못 읽음
if k-5 < 0:
    print(0)
# k가 26일 경우 모든 단어 읽기 가능
elif k-5 == 21:
    print(n)
# 그 외 dfs 수행 후 최대 갯수 출력
else:
    dfs(0, 0)
    print(answer)