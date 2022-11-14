def solution(phone_book):
    answer = True
    phone_book.sort()   # 전화번호부 정렬
    
    for idx in range(len(phone_book)-1):
        # 기준 전화번호보다 비교하는 전화번호의 길이가 길 때
        if len(phone_book[idx]) < len(phone_book[idx+1]):
            # 기준 전화번호가 접두어일 경우 False, 반복문 종료
            if phone_book[idx+1][:len(phone_book[idx])] == phone_book[idx]:
                answer = False
                break
    return answer