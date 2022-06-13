from graphs import Verge, Node, Graph

graph = Graph(name='Base Graph')
node1 = graph.create_node(name='Node-1', graph='base', bold=True)
node2 = graph.create_node(name='Node-2', graph='base')
node3 = graph.create_node(name='Node-3', graph='base', bold=True)
node4 = graph.create_node(name='Node-4', graph='base')

graph.create_verge(node1, node2, name='Verge 1V2')
graph.create_verge(node2, node3, name='Verge 2V3')
graph.create_verge(node3, node4, name='Verge 3V4')


for node in node3.search_in_nodes_tree(bold=True):
    print(node)