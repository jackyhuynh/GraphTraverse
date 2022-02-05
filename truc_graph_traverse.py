# Required library
import matplotlib.pyplot as plt
import networkx as nx

"""
# openfile read input from textfile
# In fact, I test the data on different jupiter notebook and come up with the shortest version
"""


def openfile(filename):
    with open(filename, "r") as file_reader:
        all_lines = file_reader.readlines()
    return all_lines


"""
create_data(data): take parameter data, remove all the newline, space and then convert each line to a tuple
create RoadDict dictionary and list of tuple clean_data
"""


def create_data(data):
    clean_data = []
    road_dict = {}
    count = 0
    # Clean the data by using for loop
    for line in data:
        line = line.replace('\n', '').replace(' ', '').split(',')
        road_dict[count] = {'citi1': line[0], 'citi2': line[1], 'distance': line[2]}
        clean_data.append((line[0], line[1], float(line[2])))
    return clean_data, road_dict


"""
Simple get the input from user, and validation, to make sure it not crash the application
"""


def get_user_input(cities, purpose):
    user_input = input(f"Please enter the {purpose} city: ").capitalize()
    while user_input not in cities:
        cities_display(cities)
        user_input = input(f"Please enter the {purpose} city again: ").capitalize()

    return user_input


"""
Print out the cities in the list
"""


def cities_display(cities):
    print("Target city and Destination city must be:")
    for citi in cities:
        print(citi, end=', ')

    print('')


if __name__ == '__main__':
    # Preparation:
    # create RoadDict as requirement and graph_data to feed in networkx to create graphs
    graph_data, road_dict = create_data(openfile("frenchcities.txt"))
    # create multi graph using networkx
    multi_graph = nx.MultiGraph()
    multi_graph.add_weighted_edges_from(graph_data)

    # Convert the graph to dictionary with weight
    multi_graph_dict = dict(multi_graph.degree(weight='weight'))
    # create the city list for validation only
    cities_list = list(multi_graph_dict)

    # Task 1: print out the data
    nx.draw(multi_graph, with_labels=True, font_weight='bold')
    plt.show()

    # Task 2:
    cities_display(cities_list)
    target = get_user_input(cities_list, "target")
    destination = get_user_input(cities_list, "destination")

    # Using Kilometer because it is the standard measurement in France:
    # Searching using Dijkstra Algorithm (Bread First Search)
    print(f"BFS: Cities need to travel: {nx.dijkstra_path(multi_graph, target, destination)}, "
          f"total distance: {nx.dijkstra_path_length(multi_graph, target, destination)} Km")
    # Searching using Bellman Forf Algorithm (Depth First Search)
    print(f"DFS: Cities need to travel: {nx.bellman_ford_path(multi_graph, target, destination)}, "
          f"total distance: {nx.bellman_ford_path_length(multi_graph, target, destination)} Km")
