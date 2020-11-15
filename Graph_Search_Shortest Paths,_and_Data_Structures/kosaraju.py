import random
class Node:
    def __init__(self, value):
        self.value = value
        self.next = []
        self.is_visited = False

    def set_next(self, next):
        self.next.append(next)

    def set_is_visited(self):
        self.is_visited = True


def dfs_stack(s):
    stack = []
    stack.append(s)

    while stack:
        node = stack.pop(-1)
        print(node.value)
        node.set_is_visited()
        edges = node.next

        if edges is None:
            continue

        for i in edges:
            if not i.is_visited:
                stack.append(i)


def dfs_rec(visit, g, n):
    if n not in visit:
        visit.add(n)
        dfs_rec(visit, g, g[n])


if __name__ == '__main__':

    with open("graph.txt") as tf:
        content = tf.readlines()

    removed_content = [x.strip('\n').split(' ') for x in content]

    result = [list(map(int, i)) for i in removed_content]

    graph_reversed = {}
    for k, v in result:
        graph_reversed[v] = k

    visited = set()
    while True:
        remain = graph_reversed.keys() - visited
        if remain:
            node = list(remain)[0]
            dfs_rec(visited, graph_reversed, node)
        else:
            break

    graph = {}
    for k, v in result:
        graph[k] = v

    visited_rev = set()
    while True:
        remain = visited - visited_rev
        if remain:
            leader = list(remain)[0]
            print(leader)
            dfs_rec(visited_rev, graph, leader)
        else:
            break
