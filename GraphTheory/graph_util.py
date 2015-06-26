import sys

def read_graph(file_path):
    lines = []
    with open(file_path) as file_handler:
        lines = file_handler.read().split('\n')
    
    edges = []
    max_node_index = 0
    min_node_index = sys.maxint

    for line in lines: 
        if line[0] == '#':
            continue;
        edge = [int(x) for x in line.strip().split(" ")]
        max_node_index = max(max(edge), max_node_index)
        min_node_index = min(min(edge), min_node_index)

        if len(edge) < 2:
            print 'Incorrect edge {}'.format(edge)
            return
        edges.append(edge)
    
    if (min_node_index is not 0):
        print 'Error: Graph needs to be 0 based continuous node index'
        return

    graph = [[] for _ in range(max_node_index + 1)]
    for edge in edges:
        graph[edge[0]].append(tuple(edge[1:]))

    return graph

def transpose(graph):
    tr_graph = [[] for _ in range(len(graph))]
    for index, adj_list in enumerate(graph):
        for edge in adj_list:
            out_value_tuple = (index,) + tuple(edge[1:])
            tr_graph[edge[0]].append(out_value_tuple)
            
    return tr_graph

def __dfs_find_index(graph, has_found_list, st_index, out_found_list):
    if has_found_list[st_index]:
        return
    has_found_list[st_index] = True
    #First visit all edges.
    for edge in graph[st_index]:
        if (not has_found_list[edge[0]]):
            __dfs_find_index(graph, has_found_list, edge[0], out_found_list)
    out_found_list.append(st_index) #Push index only all edges are visited

def dfs_find_index(graph, has_found_list, out_found_list):
    for index, adj_list in enumerate(graph):
        if not has_found_list[index]:
            __dfs_find_index(graph, has_found_list,index, out_found_list)
    

def main():
    g = read_graph("./graph_data.txt")
    
if __name__ == "__main__":
    main()
