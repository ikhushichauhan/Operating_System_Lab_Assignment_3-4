# Disk Scheduling Algorithms

def fcfs(requests, head):
    seek_time = 0
    for r in requests:
        seek_time += abs(head - r)
        head = r
    return seek_time


def sstf(requests, head):
    seek_time = 0
    req = requests.copy()

    while req:
        nearest = min(req, key=lambda x: abs(x - head))
        seek_time += abs(head - nearest)
        head = nearest
        req.remove(nearest)

    return seek_time


def scan(requests, head, disk_size):
    seek_time = 0
    left = [r for r in requests if r < head]
    right = [r for r in requests if r >= head]

    left.sort(reverse=True)
    right.sort()

    for r in right:
        seek_time += abs(head - r)
        head = r

    seek_time += abs(head - (disk_size - 1))
    head = disk_size - 1

    for r in left:
        seek_time += abs(head - r)
        head = r

    return seek_time


def cscan(requests, head, disk_size):
    seek_time = 0
    left = [r for r in requests if r < head]
    right = [r for r in requests if r >= head]

    left.sort()
    right.sort()

    for r in right:
        seek_time += abs(head - r)
        head = r

    seek_time += abs(head - (disk_size - 1))
    head = 0
    seek_time += disk_size - 1

    for r in left:
        seek_time += abs(head - r)
        head = r

    return seek_time


# ===== MAIN PROGRAM =====

n = int(input("Enter number of requests: "))
requests = list(map(int, input("Enter request sequence (space separated): ").split()))
head = int(input("Enter initial head position: "))
disk_size = int(input("Enter disk size: "))

print("\nTotal Seek Time:")
print("FCFS:", fcfs(requests, head))
print("SSTF:", sstf(requests, head))
print("SCAN:", scan(requests, head, disk_size))
print("C-SCAN:", cscan(requests, head, disk_size))