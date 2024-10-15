from collections import deque

n, w, L = map(int, input().split())
trucks = list(map(int, input().split()))

def chk(n, w, L, trucks):
    time = 0
    bridge = deque([0]*w)

    weight = 0
    trucks = deque(trucks)

    while trucks or weight > 0:
        time += 1
        weight -= bridge.popleft()
        if trucks:
            if weight + trucks[0] <= L:
                truck = trucks.popleft()
                bridge.append(truck)
                weight += truck
            else:
                bridge.append(0)

    return time

print(chk(n, w, L, trucks))