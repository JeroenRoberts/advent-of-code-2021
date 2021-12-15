from queue import PriorityQueue


if __name__ == "__main__":
    p = PriorityQueue()
    p.put((3, 'a'))
    p.put((4, 'b'))
    p.put((9, 'asda'))
    p.put((1, 'bsda'))
    visited = set()
    # p.put(1)
    while not p.empty():
        next_item = p.get()
        print(next_item)
    # print(p)
    # print(dir(p))
    # p.
    # PriorityQueue(7, 'b')
    # PriorityQueue(3, 'f')


