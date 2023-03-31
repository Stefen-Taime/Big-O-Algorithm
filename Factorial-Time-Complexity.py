import itertools

def tsp_brute_force(graph):
    n = len(graph)
    min_cost = float('inf')
    optimal_path = []

    for permutation in itertools.permutations(range(1, n)):
        cost = 0
        prev_city = 0
        for city in permutation:
            cost += graph[prev_city][city]
            prev_city = city
        cost += graph[prev_city][0]

        if cost < min_cost:
            min_cost = cost
            optimal_path = [0] + list(permutation) + [0]

    return min_cost, optimal_path

graph = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]
min_cost, optimal_path = tsp_brute_force(graph)
print("Minimum cost:", min_cost)
print("Optimal path:", optimal_path)
