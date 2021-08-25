t = int(input())

for num in range(1, t + 1):
    N = int(input())
    start = [0] * 5001
    end = [0] * 5001
    bus_stop = [0] * 5001

    for i in range(N):
        a, b = map(int, input().split())
        start[a] += 1
        end[b] += 1

    for i in range(len(bus_stop) - 1):
        bus_stop[i + 1] = bus_stop[i] - end[i] + start[i + 1]

    P = int(input())
    print(f'#{num}', end=' ')
    for i in range(P):
        C = int(input())
        print(bus_stop[C], end=' ')
    print()
