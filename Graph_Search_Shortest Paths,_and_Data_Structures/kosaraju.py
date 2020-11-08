class Node:
    def __init__(self, value):
        self.value = value
        self.next = []
        self.is_visited = False

    def set_next(self, next):
        self.next.append(next)

    def set_is_visited(self):
        self.is_visited = True


def dfs(node):
    stack = []
    stack.append(node)

    while stack:
        node = stack.pop(-1)
        edges = node.next

        if edges is None:
            continue

        for i in edges:
            stack.append(i)


if __name__ == '__main__':
    simple_graph = [[1, 3, 2], [2, 4], [3, 4]]
    head = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    head.set_next(node2)
    head.set_next(node3)
    node2.set_next(node4)
    node3.set_next(node4)
    dfs(head)


# if __name__ == '__main__':
#
#     with open("graph.txt") as tf:
#         content = tf.readlines()
#
#     removed_content = [x.strip('\n').split(' ') for x in content]
#
#     print(removed_content)