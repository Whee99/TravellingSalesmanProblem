from sys import maxsize

# parcel_sort takes in the optimum path and the parcel list
# it will then sorts the parcels based on the optimum path
# start of parcel_sort
def parcel_sort(parcels, optimum_path):
    parcels_sorted = []
    for i in range(len(optimum_path)):
        city_slot = []
        for j in range(len(parcels)):
            if(optimum_path[i] == parcels[j]):
                city_slot.append(parcels(j))
        parcels_sorted.append(city_slot)
    return parcels_sorted
# end of parcel_sort

# start of loading1
def loading1(parcels):
    truck = []
# end of loading1

# start of possible_route
def possible_routes(graph):
    if len(graph) == 0:
        return []
    elif len(graph) == 1:
        return [graph]

    all_routes = []
    for i in range(len(graph)):
        origin = graph[i]
        remains = graph[:i] + graph[i+1:]
        for j in possible_routes(remains):
            all_routes.append([origin] + j)

    return all_routes
# end of possible_route

# start of tsp
def tsp(graph, s):
    vertex = []
    for i in range(len(graph)):
        if i != s:
            vertex.append(i)

    min_distance = maxsize
    all_routes = possible_routes(vertex)

    distance = []
    optimum_path = []
    optimum_path_printed = []

    for i in all_routes:
        current_distance = 0

        k = s
        for j in i:
            current_distance += graph[k][j]
            k = j
        current_distance += graph[k][s]

        min_distance = min(min_distance, current_distance)
        distance.append(current_distance)

    for i in range(len(distance)):
        if distance[i] == min_distance:
            optimum_path.append(all_routes[i])

    for i in optimum_path[0]:
        if i == 1:
            optimum_path_printed.append('B')
        elif i == 2:
            optimum_path_printed.append('C')
        else:
            optimum_path_printed.append('D')

    return optimum_path_printed
# end of tsp

# 2D map
map = [[0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]]

parcels = ['B', 'D', 'C', 'B', 'C', 'C', 'B', 'B', 'D']

optimum_path = tsp(map, 0)
optimum_path.insert(0, 'A')
optimum_path.append('A')