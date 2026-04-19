# Page Replacement Algorithms (FINAL FIXED)

def fifo(pages, frames):
    memory = []
    faults = 0

    for page in pages:
        if page not in memory:
            if len(memory) < frames:
                memory.append(page)
            else:
                memory.pop(0)
                memory.append(page)
            faults += 1
    return faults


def lru(pages, frames):
    memory = []
    faults = 0

    for i in range(len(pages)):
        if pages[i] not in memory:
            if len(memory) < frames:
                memory.append(pages[i])
            else:
                last_used = []
                for m in memory:
                    if m in pages[:i]:
                        last_used.append(pages[:i][::-1].index(m))
                    else:
                        last_used.append(float('inf'))
                
                memory[last_used.index(max(last_used))] = pages[i]
            faults += 1

    return faults


def optimal(pages, frames):
    memory = []
    faults = 0

    for i in range(len(pages)):
        if pages[i] not in memory:
            if len(memory) < frames:
                memory.append(pages[i])
            else:
                future = []
                for m in memory:
                    if m in pages[i+1:]:
                        future.append(pages[i+1:].index(m))
                    else:
                        future.append(float('inf'))
                
                memory[future.index(max(future))] = pages[i]
            faults += 1

    return faults


def mru(pages, frames):
    memory = []
    faults = 0

    for i in range(len(pages)):
        if pages[i] not in memory:
            if len(memory) < frames:
                memory.append(pages[i])
            else:
                # Most recently used page replace
                for j in range(i-1, -1, -1):
                    if pages[j] in memory:
                        memory.remove(pages[j])
                        break
                memory.append(pages[i])
            faults += 1

    return faults


def second_chance(pages, frames):
    memory = []
    ref_bit = []
    faults = 0
    pointer = 0

    for page in pages:
        if page not in memory:
            while len(memory) == frames and ref_bit[pointer] == 1:
                ref_bit[pointer] = 0
                pointer = (pointer + 1) % frames

            if len(memory) < frames:
                memory.append(page)
                ref_bit.append(1)
            else:
                memory[pointer] = page
                ref_bit[pointer] = 1
                pointer = (pointer + 1) % frames

            faults += 1
        else:
            ref_bit[memory.index(page)] = 1

    return faults


# ===== MAIN PROGRAM =====

frames = int(input("Enter number of frames: "))
pages = list(map(int, input("Enter page reference string: ").split()))

print("\nPage Faults:")
print("FIFO:", fifo(pages, frames))
print("LRU:", lru(pages, frames))
print("Optimal:", optimal(pages, frames))
print("MRU:", mru(pages, frames))
print("Second Chance:", second_chance(pages, frames))