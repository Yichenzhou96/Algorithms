from random import choice


def contraction(x):
    node_list = [i[0] for i in x]

    while len(node_list) > 2:
        row = choice(node_list)-1
        choose = choice(x[row][1:])

        [x[row].append(k) for k in x[choose-1]]

        for i in x[row][1:]:
            for j in range(len(x[i-1])):
                if x[i-1][j] == choose:
                    x[i-1][j] = x[row][0]

        new = [a for a in x[row][1:] if a != x[row][0]]
        [x[row].pop(-1) for _ in range(1, len(x[row]))]
        [x[row].append(k) for k in new]
        node_list.remove(choose)

    return len(x[node_list[0]-1])-1


if __name__ == '__main__':

    mini_cut = 9999
    for _ in range(5):
        content = [[1,2,3], [2,1,3,4], [3,1,2,4], [4,2,3]]
        cut = contraction(content)

        if cut < mini_cut:
            mini_cut = cut

    print(mini_cut)
