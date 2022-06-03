from graphs import Verge, Node, Graph

graph = Graph(name='Base Graph')
node1 = graph.create_node(name='Node-1')
node2 = graph.create_node(name='Node-2')
graph.create_verge(node1, node2, name='Verge 1V2')

print(graph.get_node_by_index(0).verges)
print(list(graph.get_node_by_index(0).get_connected_nodes()))