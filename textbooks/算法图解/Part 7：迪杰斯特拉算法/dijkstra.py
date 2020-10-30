'''
Author: ZhXZhao
Date: 2020-10-30 16:54:25
LastEditors: ZhXZhao
LastEditTime: 2020-10-30 20:02:43
Description:
'''


def find_min_unpro(costs, processed):
    infinity = float("inf")
    min_value = infinity
    min_node = None
    for node in costs.keys():
        if costs[node] < min_value and node not in processed:
            min_node = node
            min_value = costs[node]
    return min_node


def get_min_path(parents, start, end):
    node = end
    path = end
    while parents[node] != start:
        node = parents[node]
        path = path + "<-" + node
    return path + "<-" + start


def dijkstra(graph, start, end):
    costs = {}
    parents = {}
    processed = []
    infinity = float("inf")
    for node in graph.keys():
        costs[node] = infinity if node not in graph[start].keys(
        ) else graph[start][node]
    for node in graph.keys():
        parents[node] = start if node in graph[start].keys() else None
    node = find_min_unpro(costs, processed)
    while node is not None:
        neiborhoods = graph[node]
        cost = costs[node]
        for n in neiborhoods.keys():
            new_costs = cost + neiborhoods[n]
            if new_costs < costs[n]:
                costs[n] = new_costs
                parents[n] = node
        processed.append(node)
        node = find_min_unpro(costs, processed)
    path = get_min_path(parents, start, end)
    return [costs[end], path]


graph = {}
graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2

graph["a"] = {}
graph["a"]["fin"] = 1

graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["fin"] = 5

graph["fin"] = {}

print(dijkstra(graph, "start", "fin")[0])
print(dijkstra(graph, "start", "fin")[1])
