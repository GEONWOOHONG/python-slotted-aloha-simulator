import random
import math
import time

def main():
    n = int(input("Enter the number of rows (n): "))
    m = int(input("Enter the number of columns (m): "))
    ADJ = [[' ' for _ in range(m)] for _ in range(n)]

    mn = int(input("Enter the minimum range of the nodes: "))
    mx = int(input("Enter the maximum range of the nodes: "))
    nodes = int(input("Enter the number of senders: "))

    random.seed(int(time.time()))

    MATRIX = [[0]*3 for _ in range(nodes)]

    for i in range(nodes):
        while True:
            x = random.randint(0, n - 1)
            y = random.randint(0, m - 1)
            if ADJ[x][y] == ' ':
                break
        ADJ[x][y] = '*'
        MATRIX[i][0] = x
        MATRIX[i][1] = y
        MATRIX[i][2] = random.randint(mn, mx - 1)

    print("\nPlacing the senders:")
    for row in ADJ:
        print(''.join(row))

    S = set()
    points = set()

    for i in range(nodes):
        x1, y1, r1 = MATRIX[i]
        for j in range(i + 1, nodes):
            x2, y2, r2 = MATRIX[j]
            dist = int(math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2))
            if dist <= r1 and dist <= r2:
                points.add((x1, y1))
                points.add((x2, y2))
                S.add(i)
                S.add(j)

    print("\nThe updated maze:")
    for i in range(n):
        line = ''
        for j in range(m):
            if (i, j) in points:
                line += '*'
            else:
                line += ' '
        print(line)

    print("\nThe SENDERS who will participate are:", ' '.join(str(s + 1) for s in sorted(S)))

    print("\n######### Using Slotted ALOHA #########\n")
    Kmax = int(input("Enter Kmax: "))
    Tp = int(input("Enter Tp: "))
    slots = int(input("Enter the number of time slots to be used: "))

    NODES = list(S)
    n_participants = len(NODES)
    Kvals = [0] * (nodes + 1)
    WaitTime = [0] * (nodes + 1)
    total = 0
    eff = 0

    for i in range(slots):
        print("SLOT=" + str(i + 1))
        for j in range(n_participants):
            if WaitTime[NODES[j]] > 0:
                WaitTime[NODES[j]] -= 1

        TOSEND = []
        for k in range(n_participants):
            if WaitTime[NODES[k]] == 0 and random.randint(0, 1):
                TOSEND.append(NODES[k])

        sz = len(TOSEND)
        total += sz

        if sz > 1:
            print("Collision occurred!!!")
            for sender in TOSEND:
                Kvals[sender] += 1
                if Kvals[sender] > Kmax:
                    print(f"Aborting sender {sender + 1}'s packet.")
                    Kvals[sender] = 0
                    WaitTime[sender] = 0
                else:
                    w = random.randint(1, Kmax)
                    WaitTime[sender] = w
                    print(f"Sender {sender + 1} Blocked. (waits for {w} time slots, K={Kvals[sender]})")
                    WaitTime[sender] += 1
        elif sz == 1:
            print(f"Sender {TOSEND[0] + 1}'s packet successfully transmitted!")
            eff += 1
            WaitTime[TOSEND[0]] = 0
            Kvals[TOSEND[0]] = 0
        print()

    print("Total number of packets=" + str(total))
    print("Total number of packets sent=" + str(eff))

if __name__ == "__main__":
    main()