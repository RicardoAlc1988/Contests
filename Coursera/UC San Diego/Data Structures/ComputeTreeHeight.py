import sys
from collections import deque
#sys.setrecursionlimit(10 ** 7)

class TreeNode:

    def __init__(self, key, childs):
        self.key = key
        self.childs = childs
        self.depth = None

    def add_child(self, child):
        self.childs.append(child)

class Tree:

    def __init__(self, root: TreeNode):
        self.root = root
        self.root.level = 1

    def get_height(self):
        level = 1
        tree_childs = deque()
        tree_childs.append(self.root)
        while tree_childs:
            parent = tree_childs.popleft()
            for child in parent.childs:
                child.level = parent.level + 1
                tree_childs.append(child)
                if child.level > level:
                    level = child.level
        return level



def compute_tree_height(n: int, parents):
    nodes = [TreeNode(i, []) for i in range(n)]
    for i, parent in enumerate(parents):
        if parent == -1:
            tree = Tree(nodes[i])
            #print(tree)
        else:
            nodes[parent].childs.append(nodes[i])
    #for i in range(n):
    #    print(nodes[i].key)
    #    print([node.key for node in nodes[i].childs])
    return tree.get_height()

def main():
    n = int(input())
    parents_in = sys.stdin.readline()
    parents = list(map(int, parents_in.split()))
    print(compute_tree_height(n, parents))


if __name__ == "__main__":
    main()