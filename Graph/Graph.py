class Graph:
    def __init__(self, edges) -> None:
        self.edges = edges
        self.graph_dict = {}
        for start, end in self.edges:
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start] = [end]

    def find_all_routes(self, start, end, path=[]):
        path = path + [start]
        if start == end:
            return [path]

        if start not in self.graph_dict:
            return []

        paths = []
        for start_dest in self.graph_dict[start]:
            if start_dest not in path:
                new_paths = self.find_all_routes(start_dest, end, path)
                for p in new_paths:
                    paths.append(p)

        return paths

    def get_shortest_path(self, start, end):
        return min(self.find_all_routes(start, end))

if __name__ == "__main__":
    routes = [
        ("Mumbai", "Paris"),
        ("Mumbai", "Dubai"),
        ("Paris", "Dubai"),
        ("Paris", "New York"),
        ("Dubai", "New York"),
        ("New York", "Toronto"),
    ]

    route_graph = Graph(routes)

    print (route_graph.graph_dict)

    start = "Mumbai"
    end = "New York"
    print (f"All routes between {start} and {end}:", route_graph.find_all_routes(start, end))
    print (f"Shortest route between {start} and {end}:", route_graph.get_shortest_path(start, end))