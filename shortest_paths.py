import heapq


class WeightedGraph:
    def __init__(self):
        self.adjacency_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []

    def add_edge(self, source, destination, weight):
        self.add_vertex(source)
        self.add_vertex(destination)

        self.adjacency_list[source].append((destination, weight))

    def dijkstra(self, source):
        distances = {
            vertex: float("inf")
            for vertex in self.adjacency_list
        }

        distances[source] = 0
        priority_queue = [(0, source)]

        while priority_queue:
            current_distance, current_vertex = heapq.heappop(
                priority_queue
            )

            if current_distance > distances[current_vertex]:
                continue

            for neighbor, weight in self.adjacency_list[current_vertex]:
                new_distance = current_distance + weight

                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance

                    heapq.heappush(
                        priority_queue,
                        (new_distance, neighbor)
                    )

        return distances

    def bellman_ford(self, source):
        distances = {
            vertex: float("inf")
            for vertex in self.adjacency_list
        }

        distances[source] = 0

        vertices = list(self.adjacency_list.keys())
        edges = []

        for source_vertex in self.adjacency_list:
            for destination, weight in self.adjacency_list[source_vertex]:
                edges.append(
                    (source_vertex, destination, weight)
                )

        for _ in range(len(vertices) - 1):
            updated = False

            for start, end, weight in edges:
                if distances[start] != float("inf"):
                    new_distance = distances[start] + weight

                    if new_distance < distances[end]:
                        distances[end] = new_distance
                        updated = True

            if not updated:
                break

        negative_cycle = False

        for start, end, weight in edges:
            if distances[start] != float("inf"):
                if distances[start] + weight < distances[end]:
                    negative_cycle = True
                    break

        return distances, negative_cycle


def test_nonnegative_graph():
    print("\nTEST GRAPH 1: Nonnegative Weights")

    graph = WeightedGraph()

    graph.add_edge("A", "B", 4)
    graph.add_edge("A", "C", 2)
    graph.add_edge("C", "B", 1)
    graph.add_edge("B", "D", 5)
    graph.add_edge("C", "D", 8)
    graph.add_edge("D", "E", 2)
    graph.add_edge("C", "E", 10)

    print("Source Vertex: A")

    dijkstra_result = graph.dijkstra("A")
    bellman_result, negative_cycle = graph.bellman_ford("A")

    print("Dijkstra:")
    print(dijkstra_result)

    print("Bellman-Ford:")
    print(bellman_result)

    print("Negative Cycle Detected:", negative_cycle)


def test_negative_edge_graph():
    print("\nTEST GRAPH 2: Negative Edge, No Negative Cycle")

    graph = WeightedGraph()

    graph.add_edge("A", "B", 4)
    graph.add_edge("A", "C", 5)
    graph.add_edge("B", "C", -2)
    graph.add_edge("C", "D", 3)

    print("Source Vertex: A")

    bellman_result, negative_cycle = graph.bellman_ford("A")

    print("Bellman-Ford:")
    print(bellman_result)

    print("Negative Cycle Detected:", negative_cycle)


def test_negative_cycle_graph():
    print("\nTEST GRAPH 3: Negative Cycle")

    graph = WeightedGraph()

    graph.add_edge("A", "B", 1)
    graph.add_edge("B", "C", -2)
    graph.add_edge("C", "A", -2)

    print("Source Vertex: A")

    bellman_result, negative_cycle = graph.bellman_ford("A")

    print("Bellman-Ford:")
    print(bellman_result)

    print("Negative Cycle Detected:", negative_cycle)


if __name__ == "__main__":
    test_nonnegative_graph()
    test_negative_edge_graph()
    test_negative_cycle_graph()
