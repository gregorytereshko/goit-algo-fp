import networkx as nx
import matplotlib.pyplot as plt
import uuid
import heapq


class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())


def build_heap_tree(heap_array):
    root = Node(heap_array[0])
    heap_queue = [(root, 0)]
    idx = 0
    while idx < len(heap_array):
        parent, parent_idx = heap_queue.pop(0)
        left_idx = 2 * parent_idx + 1
        right_idx = 2 * parent_idx + 2
        if left_idx < len(heap_array):
            parent.left = Node(heap_array[left_idx])
            heap_queue.append((parent.left, left_idx))
        if right_idx < len(heap_array):
            parent.right = Node(heap_array[right_idx])
            heap_queue.append((parent.right, right_idx))
        idx += 1
    return root


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        # Використання id та збереження значення вузла
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


def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(
        data=True)}  # Використовуйте значення вузла для міток

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False,
            node_size=2500, node_color=colors)
    plt.show()


# Припустимо, що у нас є бінарна купа у вигляді масиву
heap_array = [1, 3, 5, 7, 9, 2, 4, 34, 2, 1, 2]
heapq.heapify(heap_array)

# Побудова дерева з купи
heap_tree_root = build_heap_tree(heap_array)

# Відображення бінарної купи у вигляді дерева
draw_tree(heap_tree_root)
