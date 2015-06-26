import graph_util

def __dfs(graph, has_found_list, index):
    has_found_list[index] = True    
    print 'Index is: {}'.format(index)   
    for edge in graph[index]:
        if (not has_found_list[edge[0]]):
            __dfs(graph, has_found_list, edge[0])


def main():
    g = graph_util.read_graph("./graph_data.txt")
    print 'Original graph {}'.format(g)

    tr_graph = graph_util.transpose(g)
    print 'Transpose graph {}'.format(tr_graph)

    has_found_list = [False for _ in range(len(tr_graph))]

    out_found_list = []
    graph_util.dfs_find_index(g, has_found_list, out_found_list)

    print 'Out Found List: {}'.format(out_found_list)

    has_found_list = [False for _ in range(len(tr_graph))]

    for index in out_found_list[::-1]:
        if not has_found_list[index]:
            print 'Connected componet is: '
            __dfs(tr_graph, has_found_list, index)

    
if __name__ == '__main__':
    main()
