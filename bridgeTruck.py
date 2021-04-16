from collections import deque
import math


def solution(bridge_length, weight, truck_weights):
    answer = 0
    go_throwing_truck = deque([0] * bridge_length)
    truck_weights = deque(truck_weights)
    while True:
        if len(truck_weights) != 0:
            if sum(go_throwing_truck) <= weight:
                go_throwing_truck.popleft()
                go_throwing_truck.append(truck_weights.popleft())
                answer += 1
            else:
                go_throwing_truck.popleft()
                go_throwing_truck.append(0)
                answer += 1
        else:
            if sum(go_throwing_truck) != 0:
                go_throwing_truck.popleft()
                go_throwing_truck.append(0)
                answer += 1
            else:
                break
    return answer


length = [2, 100, 100]
bridge_weight = [10, 100, 100]
truck_weight_test = [[7, 4, 5, 6], [10], [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]]
print(solution(length[0], bridge_weight[0], truck_weight_test[0]))
