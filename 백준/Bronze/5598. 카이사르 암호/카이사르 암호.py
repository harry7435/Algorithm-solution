import sys
input = sys.stdin.readline

word = input().rstrip()
new_word = ""
# 아스키코드 변환 후 -3
for w in word:
    change_ord = ord(w)-3
    # A(65)보다 작으면 다시 Z(90) 루프
    if change_ord < 65:
        change_ord += 26
    new_word += chr(change_ord)
# 출력
print(new_word, end="")