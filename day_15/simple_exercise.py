from queue import PriorityQueue

def print_queue(q):
    print(list(q.queue))


if __name__ == "__main__":
    cost = {}
    cost[('A', 'B')] = 2
    cost[('A', 'D')] = 4
    cost[('A', 'F')] = 0
    cost[('F', 'B')] = 2
    cost[('F', 'G')] = 0
    cost[('C', 'G')] = 1
    cost[('D', 'C')] = 3
    cost[('B', 'C')] = 5
    for k, v in cost.copy().items():
        cost[k[1], k[0]] = v

    all = set(['A', 'B', 'C', 'D', 'F', 'G'])
    visited = set()
    start = 'A'
    current = start
    visited.add(start)
    cost_from_A_to_point = {}
    shortest_paths_from_A_to_point = {}
    for a in all:
        if a != start:
            cost_from_A_to_point[a] = 44444444 #=infinity
        else:
            cost_from_A_to_point[a] = 0
        shortest_paths_from_A_to_point[a] = ['A']

    unvisited_nodes = all
    print(unvisited_nodes)


    while unvisited_nodes: #Remember that Dijkstra’s algorithm executes until it visits all the nodes in a graph, so we’ll represent this as a condition for exiting the while-loop. https://www.udacity.com/blog/2021/10/implementing-dijkstras-algorithm-in-python.html
        print(f'{ current = }')
        p = PriorityQueue()
        for r in cost.keys():
            if r[0] == current:
                print(f'{r[1]}', 'is a neighbour of current', f'{current}')
                if r[1] in unvisited_nodes:
                    new_cost = cost_from_A_to_point[r[0]] + cost[r]
                    if new_cost < cost_from_A_to_point[r[1]]:
                        cost_from_A_to_point[r[1]] = new_cost
                        shortest_paths_from_A_to_point[r[1]] = shortest_paths_from_A_to_point[r[0]] + [r[1]]
                        p.put((new_cost, r[1]))
                    else:
                        p.put((cost_from_A_to_point[r[1]], r[1])) #bug here maybe
        print_queue(p)
        unvisited_nodes.remove(current)
        if current == 'G':
            print('found shortest route to G')
            print(shortest_paths_from_A_to_point[current])
            break
        else:
            current = p.get()[1]

        #find neighbour with least cost
        # while not p.empty():
        #     cost, path = p.get()
        #     new_cost = cost_from_A_to_point[path[0]] + cost
        #     if new_cost < cost_from_A_to_point[path[1]]:
        #         cost_from_A_to_point[path[1]] = new_cost
        #         shortest_paths_from_A_to_point[path[1]] = shortest_paths_from_A_to_point[path[0]] + [path[1]]

            # print(cost, path)

        # for r in cost.keys():
        #     if r[0] == current:
        #         if r[1] not in visited:
        #             new_cost = cost_from_A_to_point[r[0]] + cost[r] 
        #             if new_cost < cost_from_A_to_point[r[1]]:
        #                 cost_from_A_to_point[r[1]] = new_cost
        #                 shortest_paths_from_A_to_point[r[1]] = shortest_paths_from_A_to_point[r[0]] + [r[1]]
        #                 current = r[1]
        #                 visited.add(r[1])
        #             else:
        #                 print('path ', r, 'unexplored too costly ', f'{new_cost = }')




    # visited = set()
    # p.put((3, 'a'))
    # p.put((4, 'b'))
    # p.put((9, 'asda'))
    # p.put((1, 'bsda'))
    # p.put(1)
    # while not p.empty():
    #     next_item = p.get()
        # print(next_item)
    # print(p)
    # print(dir(p))
    # p.
    # PriorityQueue(7, 'b')
    # PriorityQueue(3, 'f')


