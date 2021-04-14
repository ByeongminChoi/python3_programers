##배열의 방을 한칸의 계단이라고 가정
# i번째 칸에 cost[i] 양수의 비용이 할당
# 비용을 지불하게 되면 1칸 또는 2칸 이동가능
# 시작시 0번째 또는 1첫번째에서 시작가능
# 끝까지 이동했을때 발생하는 비용이 최소비용이 되도록 해야한다.
import math


def min_cost_step(cost):
    case1, case2, current = 0, 0, 0
    for i in range(len(cost)):
        if i == 0:
            current = cost[-1] + min(case1, case2)
            case2 = case1
            case1 = current
        else:
            current = cost[-(i + 1)] + min(case1, case2)
            case2 = case1
            case1 = current
    return min(case1, case2)


test = [[10, 15, 20], [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]]
print(min_cost_step(test[1]))
