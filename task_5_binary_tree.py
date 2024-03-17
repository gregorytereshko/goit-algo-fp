import uuid
import networkx as nx
import matplotlib.pyplot as plt


class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r,
                          y=y - 1, layer=layer + 1)
    return graph


def draw_tree(tree_root, traversal_order):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = []
    for node_id in tree.nodes():
        # Визначення кольору в залежності від порядку обходу
        alpha = traversal_order.index(node_id) / len(traversal_order)
        # Створення RGB кольору
        color = f"#{int(255 * alpha):02X}{int(255 * (1 - alpha)):02X}00"
        colors.append(color)

    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False,
            node_size=2500, node_color=colors)
    plt.show()


# Створення дерева
root = Node(0)
root.left = Node(4)
root.left.left = Node(5)
root.left.right = Node(10)
root.right = Node(1)
root.right.left = Node(3)

# Обходи дерева


def dfs_traversal(node, order):
    if node:
        order.append(node.id)
        dfs_traversal(node.left, order)
        dfs_traversal(node.right, order)


def bfs_traversal(node, order):
    queue = [node]
    while queue:
        current = queue.pop(0)
        order.append(current.id)
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)


dfs_order = []
dfs_traversal(root, dfs_order)

bfs_order = []
bfs_traversal(root, bfs_order)

# Відображення дерева з обходами
draw_tree(root, dfs_order)  # Обхід у глибину
draw_tree(root, bfs_order)  # Обхід у ширину
