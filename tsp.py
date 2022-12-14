from sys import maxsize

# sorts parcels based on the optimum route
# start of parcel_sort
def parcel_sort(parcels, optimum_path):
    parcels_sorted = []
    for i in range(len(optimum_path)):
        city_slot = []
        for j in range(len(parcels)):
            if optimum_path[i] in parcels[j]:
                city_slot.append(parcels[j])
        parcels_sorted.append(city_slot)
    return parcels_sorted
# end of parcel_sort

# parcel loading for a one door truck
# start of loading1
def one_door_loading(sorted_parcels):
    truck = []
    for i in sorted_parcels:
        truck.insert(0, i)
    return truck
# end of loading1

# parcel unloading for a one door truck
# start of unloading1
def one_door_unloading(truck):
    while len(truck) != 0:
        truck.pop()
        print("Remaining parcels: {}".format(truck))
# end of unloading1

# parcel loading for a two door truck
# start of loading2
def two_door_loading(sorted_parcels):
    truck = []
    door1 = []
    door2 = []
    for i in range(len(sorted_parcels)):
        if i % 2 == 0:
            door1.insert(0, sorted_parcels[i])
        else:
            door2.insert(0, sorted_parcels[i])
    truck.append(door1)
    truck.append(door2)
    return truck
# end of loading2

# parcel unloading for a two door truck
# start of unloading2
def two_door_unloading(truck):
    i = 0
    while len(truck[0]) != 0 or len(truck[1]) != 0:
        if(i % 2 == 0):
            truck[0].pop()
        else:
            truck[1].pop()
        i += 1
        print("Door one's remaining parcels: {}".format(truck[0]))
        print("Door two's remaining parcels: {}".format(truck[1]))
# end of unloading2

# generates all possible routes
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

# travelling salesman problem algorithm
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

# parcels list
parcels = ['B', 'D', 'C', 'B', 'C', 'C', 'B', 'B', 'D']

optimum_path = tsp(map, 0)
optimum_path.insert(0, 'A')
optimum_path.append('A')

print("The optimum path is {}".format(optimum_path))
sorted_parcels = parcel_sort(parcels, tsp(map, 0))

while True:
    user_input = input("Enter 1 or 2 for the number of doors you want for your truck or 'exit' to terminate the program: ")

    if user_input.isdigit() == False:
        if user_input.lower() == "exit":
            print("Program ended.")
            break
        else:
            print("Input must be a number or 'exit'.")
    elif int(user_input) == 1:
        truck = one_door_loading(sorted_parcels)
        print("Loaded parcels on the truck: {}".format(truck))
        one_door_unloading(truck)
    elif int(user_input) == 2:
        truck = two_door_loading(sorted_parcels)
        print("Loaded parcels in door one: {}".format(truck[0]))
        print("Loaded parcels in door two: {}".format(truck[1]))
        two_door_unloading(truck)
    else:
        print("Invalid number.")