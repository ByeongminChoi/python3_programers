# 카카오 인턴 : 키패드 누르기
"""
이 전화 키패드에서 왼손과 오른손의 엄지손가락만을 이용해서 숫자만을 입력하려고 합니다.
맨 처음 왼손 엄지손가락은 * 키패드에 오른손 엄지손가락은 # 키패드 위치에서 시작하며, 엄지손가락을 사용하는 규칙은 다음과 같습니다.
엄지손가락은 상하좌우 4가지 방향으로만 이동할 수 있으며 키패드 이동 한 칸은 거리로 1에 해당합니다.
왼쪽 열의 3개의 숫자 1, 4, 7을 입력할 때는 왼손 엄지손가락을 사용합니다.
오른쪽 열의 3개의 숫자 3, 6, 9를 입력할 때는 오른손 엄지손가락을 사용합니다.
가운데 열의 4개의 숫자 2, 5, 8, 0을 입력할 때는 두 엄지손가락의 현재 키패드의 위치에서 더 가까운 엄지손가락을 사용합니다.
4-1. 만약 두 엄지손가락의 거리가 같다면, 오른손잡이는 오른손 엄지손가락, 왼손잡이는 왼손 엄지손가락을 사용합니다.
순서대로 누를 번호가 담긴 배열 numbers, 왼손잡이인지 오른손잡이인 지를 나타내는 문자열 hand가 매개변수로 주어질 때, 각 번호를 누른 엄지손가락이 왼손인 지 오른손인 지를 나타내는 연속된 문자열 형태로 return 하도록 solution 함수를 완성해주세요.
"""

# 좌표의 거리를 계산하는게 아니라 이동 한 칸당 거리 1이다. x, y 좌표의 합으로 계산하면?
from math import dist


def solution(numbers, hand):
    answer = ""

    dict_key = {
        1: ("L", (-1, 3)),
        4: ("L", (-1, 2)),
        7: ("L", (-1, 1)),
        3: ("R", (1, 3)),
        6: ("R", (1, 2)),
        9: ("R", (1, 1)),
        2: ("NULL", (0, 3)),
        5: ("NULL", (0, 2)),
        8: ("NULL", (0, 1)),
        0: ("NULL", (0, 0)),
    }

    cur_r = (1, 0)
    cur_l = (-1, 0)
    # tmp = []

    for key in numbers:
        if key in [2, 5, 8, 0]:
            # 거리로 계산
            # if dist(cur_r, dict_key[key][1]) < dist(cur_l, dict_key[key][1]):
            #     answer += "R"
            #     cur_r = dict_key[key][1]
            # elif dist(cur_r, dict_key[key][1]) > dist(cur_l, dict_key[key][1]):
            #     answer += "L"
            #     cur_l = dict_key[key][1]
            if (abs((cur_r[0] - dict_key[key][1][0])) + abs((cur_r[1] - dict_key[key][1][1]))) < (abs((cur_l[0] - dict_key[key][1][0])) + abs((cur_l[1] - dict_key[key][1][1]))):
                answer += "R"
                cur_r = dict_key[key][1]
            elif (abs((cur_r[0] - dict_key[key][1][0])) + abs((cur_r[1] - dict_key[key][1][1]))) > (abs((cur_l[0] - dict_key[key][1][0])) + abs((cur_l[1] - dict_key[key][1][1]))):
                answer += "L"
                cur_l = dict_key[key][1]
            else:
                if hand == "right":
                    answer += "R"
                    cur_r = dict_key[key][1]
                else:
                    answer += "L"
                    cur_l = dict_key[key][1]
        else:
            answer += dict_key[key][0]
            if dict_key[key][0] == "L":
                cur_l = dict_key[key][1]
            else:
                cur_r = dict_key[key][1]
            # tmp.append(key)
    return answer


nums = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hand = "right"

print(solution(nums, hand))

# dict_key = {
#         1: ("L", (1, 1)),
#         4: ("L", 2),
#         7: ("L", 3),
#         3: ("R", 1),
#         6: ("R", 2),
#         9: ("R", 3),
#         2: 1,
#         5: 2,
#         8: 3,
#         0: 4}
#
# key = 2
# print(abs(dict_key[1][1][0]))
