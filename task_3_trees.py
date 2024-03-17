import heapq
import networkx as nx
import matplotlib.pyplot as plt


def dijkstra(graph, start):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    pq = [(0, start)]
    paths = {start: [start]}

    while pq:
        current_distance, current_vertex = heapq.heappop(pq)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
                paths[neighbor] = paths[current_vertex] + [neighbor]

    return distances, paths


# Приклад графу
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

# Використовуємо networkx для побудови графа
G = nx.Graph()
for node in graph:
    G.add_node(node)
    for neighbor, weight in graph[node].items():
        G.add_edge(node, neighbor, weight=weight)

# Визначаємо початкову вершину та обчислюємо найкоротші відстані та шляхи
start_vertex = 'A'
shortest_distances, shortest_paths = dijkstra(graph, start_vertex)

# Побудова графа
pos = nx.spring_layout(G)  # Позиції вершин для візуалізації
nx.draw(G, pos, with_labels=True, node_size=2000,
        node_color='skyblue', font_size=10, font_weight='bold')

# Додаємо ваги ребер
edge_labels = {(n1, n2): d['weight'] for n1, n2, d in G.edges(data=True)}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red')

# Вивід найкоротших шляхів
for vertex, distance in shortest_distances.items():
    if vertex != start_vertex:
        path = shortest_paths[vertex]
        print(
            f'Найкоротший шлях від {start_vertex} до {vertex}: {path} з довжиною {distance}')

plt.title('Граф та найкоротші шляхи')
plt.show()
