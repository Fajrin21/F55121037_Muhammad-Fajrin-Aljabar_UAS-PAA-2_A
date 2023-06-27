import networkx as nx
import time

def tsp_shortest_path(graph, start, end):
    start_time = time.time()

    shortest_path = nx.approximation.traveling_salesman_problem(graph, weight='weight', cycle=True)

    end_time = time.time()
    return shortest_path, end_time - start_time

def dijkstra_shortest_path(graph, start, end):
    start_time = time.time()

    shortest_path = nx.dijkstra_path(graph, start, end, weight='weight')

    end_time = time.time()
    return shortest_path, end_time - start_time

def print_iterations(iterations):
    print("Iterasi:")
    for i, path in enumerate(iterations):
        print(f"Iterasi {i + 1}: {path}")

def print_execution_time(time_taken):
    print(f"Waktu komputasi: {time_taken:.6f} detik")

def print_shortest_path(path):
    print("Hasil akhir (Shortest Path):")
    print(path)

def analyze_algorithm():
    graph = nx.Graph()
    graph.add_edge('A', 'B', weight=12)
    graph.add_edge('A', 'C', weight=10)
    graph.add_edge('A', 'G', weight=12)
    graph.add_edge('B', 'C', weight=8)
    graph.add_edge('B', 'D', weight=12)
    graph.add_edge('C', 'D', weight=11)
    graph.add_edge('C', 'E', weight=3)
    graph.add_edge('C', 'G', weight=9)
    graph.add_edge('D', 'E', weight=11)
    graph.add_edge('D', 'F', weight=10)
    graph.add_edge('E', 'F', weight=6)
    graph.add_edge('E', 'G', weight=7)
    graph.add_edge('F', 'G', weight=9)

    while True:
        print("Selamat Datang di Program UAS PAA Kelas A")
        print("Dibuat Oleh:")
        print("Muhammad Fajrin Aljabar")
        print("F55121037")
        print("Graf yang tersedia:")
        print(graph.edges())
        print("Algoritma yang tersedia:")
        print("1. TSP")
        print("2. Dijkstra")
        print("3. Exit")

        choice = input("Ingin menggunakan algoritma yang mana (1/2/3): ")

        if choice == "1":
            shortest_path, time_taken = tsp_shortest_path(graph, 'A', 'G')
            print("Hasil TSP:")
            print_iterations(shortest_path)
            print_execution_time(time_taken)
            print_shortest_path(shortest_path)
        elif choice == "2":
            shortest_path, time_taken = dijkstra_shortest_path(graph, 'A', 'G')
            print("Hasil Dijkstra:")
            print_iterations([shortest_path])
            print_execution_time(time_taken)
            print_shortest_path(shortest_path)
        elif choice == "3":
            break
        else:
            print("Silahkan pilih antara 1,2 dan 3")

if __name__ == '__main__':
    analyze_algorithm()
