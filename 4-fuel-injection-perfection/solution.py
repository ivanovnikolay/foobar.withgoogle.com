def solution(n):
    count = 0
    while n:
        print(n)
        count += 1
        n = n >> 1
    print(1 << count - 1)
    print(1 << count)

solution(11)