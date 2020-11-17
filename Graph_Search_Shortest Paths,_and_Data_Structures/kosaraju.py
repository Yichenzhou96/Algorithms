import random
class Node:
    def __init__(self, value):
        self.value = value
        self.next = []
        self.is_visited = False
        self.finishing_time = 0

    def set_next(self, next):
        self.next.append(next)

    def set_is_visited(self):
        self.is_visited = True

    def set_finishing_time(self, t):
        self.finishing_time = t


def dfs_rec(visit, g, n):
    if n not in visit:
        visit.add(n)
        dfs_rec(visit, g, g[n][0])

    global t
    g[n][1] = t
    t += 1


if __name__ == '__main__':

    with open("graph.txt") as tf:
        content = tf.readlines()

    removed_content = [x.strip('\n').split(' ') for x in content]

    result = [list(map(int, i)) for i in removed_content]

    graph_reversed = {}
    for k, v in result:
        graph_reversed[v] = [k, 0]

    visited = set()
    t = 0
    for remain in graph_reversed.keys():
        if remain not in visited:
            dfs_rec(visited, graph_reversed, remain)

    graph_2 = {v[0]: [k, v[1]] for k, v in sorted(graph_reversed.items(), key=lambda item: item[1][1], reverse=True)}

    visited_2 = set()
    leader = set()
    for remain in graph_2.keys():
        if remain not in visited_2:
            leader.add(remain)
            dfs_rec(visited_2, graph_2, remain)

    print(leader)