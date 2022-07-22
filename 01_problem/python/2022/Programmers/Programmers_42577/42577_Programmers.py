import heapq


def solution(phone_book):
    # heap을 사용하여 앞이 작은 것이 0번 index가 되도록 변환
    heapq.heapify(phone_book)
    while len(phone_book) > 1:
        now = heapq.heappop(phone_book)
        if now == phone_book[0][:len(now)]:
            return False
    return True


# 풀이2: sort()를 사용하여 앞이 작은 순서로 정렬
# def solution(phone_book):
#     phone_book.sort()
#
#     for i in range(len(phone_book) - 1):
#         now = phone_book[i]
#         if now == phone_book[i+1][:len(now)]:
#             return False
#     return True


print(solution(["119", "97674223", "1195524421"]))
