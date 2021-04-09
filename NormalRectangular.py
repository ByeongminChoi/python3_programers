import math


def solution(w, h):
    answer = 0
    if w == h:
        answer = (w * h - w)
    elif w == 1 or h == 1:
        answer = 0
    else:
        for i in range(1, w):
            answer += math.floor(h - (h / w) * i)
        answer = 2 * answer

    return answer


def gcd(a, b): return b if (a == 0) else gcd(b%a, a)
def solution2(w, h): return w * h - w - h + gcd(w, h)


print(solution(3, 3))
