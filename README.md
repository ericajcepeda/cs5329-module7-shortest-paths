# CS 5329 Module 7: Shortest-Path Algorithms

## Name: Erica Cepeda
## Course: CS 5329 


## Assignment Overview
This assignment provides an implementation and comparison of two shortest-path algorithms for a weighted graph:
- Dijkstra's algorithm
- Bellman-Ford algorithm

The program uses an adjacency list representation for the weighted directed graph. This program demonstrates shortest path calculations, edge relaxation, priority queue operations, and negative edge and negative cycle detection.

## Repository Files
- `shortest_paths.py` - Python implementation of the weighted graph, Dijkstra's algorithm, Bellman-Ford algorithm, and test cases
- `README.md` - Project description and instructions
- `report.md` - Description of the algorithms and results of the tests
- `program-output.png` - Screenshot that shows successful execution of the program and the results of required tests


## Requirements
Python 3 is needed. No external libraries are used in the program. Only Python standard library is needed.

## How to Run
Run the program in the repository directory:

```bash
python3 shortest_paths.py
```

or

```bash
python shortest_paths.py
```

## Weighted Graph Representation
In this program, a weighted directed graph is represented by an adjacency list. Each vertex of the graph is kept as a key in Python dictionary. Each key contains a list of neighboring vertices and the corresponding edge weights. For example:

```python
"A": [("B", 4), ("C", 2)]
```

This represents two directed edges:
- A to B with weight 4
- A to C with weight 2

## Algorithms Used
### Dijkstra’s Algorithm
Dijkstra’s algorithm computes shortest paths from one source vertex to all other reachable vertices with non-negative weights. The program uses `heapq` library of Python as the priority queue.

### Bellman-Ford Algorithm
Bellman-Ford computes the shortest paths from one source vertex to all other reachable vertices. In contrast to Dijkstra’s algorithm, Bellman-Ford handles negative edges as well. Bellman-Ford computes a reachable negative cycle if any exists in the graph.

## Test Graphs
### Test Graph 1: Non-negative Weights
Test graph 1 consists of five vertices and all non-negative edges only. Dijkstra’s algorithm and Bellman-Ford are tested using source vertex A. Expected and observed shortest-path distances:

```text
A = 0
B = 3
C = 2
D = 8
E = 10
```

Both algorithms produced the result. Negative cycle detected:

```text
False
```

### Test Graph 2: Negative Edge, No Negative Cycle
The second graph contains an edge:

```text
B -> C = -2
```

Bellman-Ford is used because the graph contains a negative edge. Observed shortest-path distances from A:

```text
A = 0
B = 4
C = 2
D = 5
```

Negative cycle detected:
```text
False
```

### Test Graph 3: Negative Cycle
The third graph contains the cycle:

```text
A -> B = 1
B -> C = -2
C -> A = -2
```

The total weight of this cycle is:

```text
1 + (-2). -2) = -3
```

Because the cycle has a total weight Bellman-Ford detects a negative cycle. Program output:

```text
Negative Cycle Detected: True
```

The distance values continue decreasing because traveling around the cycle repeatedly produces a lower total cost.


## Program Output Evidence
A screenshot of the program execution is included in the repository:


```text
program-output.png
```


The screenshot shows:
- Dijkstras output for the nonnegative graph
- Bellman-Fords output for the nonnegative graph
- Bellman-Fords output, for the graph containing a negative edge
- Bellman-Ford negative cycle detection
- Correct `True` and `False` negative-cycle results


## Runtime Analysis
Dijkstras algorithm using a priority queue has an expected runtime of:

```text
O((V + E) log V)
```

Bellman‑Ford has an expected runtime of:

```text
O(VE)
```

where:
- `V`'s the number of vertices
- `E` is the number of edges


## Summary
Dijkstra’s algorithm is a good choice when all edge weights are nonnegative because Dijkstra’s algorithm quickly chooses the next closest vertex using a priority queue. Bellman‑Ford is more flexible because Bellman‑Ford supports edge weights and can detect negative cycles although Bellman‑Ford has a slower runtime. The three test graphs demonstrate the situations in which Dijkstra’s algorithm's appropriate and the situations, in which Bellman‑Ford is appropriate.
