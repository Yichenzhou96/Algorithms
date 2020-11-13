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


def dfs_rec(visited, graph, node):
    if node not in visited:
        visited.append(node)
        dfs_rec(visited, graph, graph[node])


if __name__ == '__main__':

    with open("graph.txt") as tf:
        content = tf.readlines()

    removed_content = [x.strip('\n').split(' ') for x in content]

    result = [list(map(int, i)) for i in removed_content]

    graph = {}
    for k, v in result:
        graph[k] = v

    visited = []
    while True:
        remain = graph.keys() - visited
        if remain:
            node = random.choice(tuple(remain))
            dfs_rec(visited, graph, node)
        else:
            break

    print(visited)
