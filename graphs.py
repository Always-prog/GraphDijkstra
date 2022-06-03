from typing import List, Dict, Iterable


class Node:
    def __init__(self, verges: List = None, **node_data):
        if not verges:
            verges = []
        self._node_data = node_data
        self.verges = verges

    def get_connected_nodes(self):
        for verge in self.verges:
            yield verge.node2 if verge.node2 is not self else verge.node1

    def get_verges(self):
        return self.verges


class Verge:
    def __init__(self, node1: Node, node2: Node, **verge_data):
        self._node1 = node1
        self._node2 = node2

        self.node1 = node1
        self.node2 = node2
        self.verge_data = verge_data

    @property
    def node1(self):
        return self._node1

    @property
    def node2(self):
        return self._node2

    @node1.setter
    def node1(self, node1_input_value):
        if not isinstance(node1_input_value, Node):
            raise ValueError(f'Cant connect first node {node1_input_value}. Incorrect type. It can be only Node')
        node1_input_value.verges.append(self)

    @node2.setter
    def node2(self, node2_input_value):
        if not isinstance(node2_input_value, Node):
            raise ValueError(f'Cant connect second node {node2_input_value}. Incorrect type. It can be only Node')
        node2_input_value.verges.append(self)


class Graph:
    def __init__(self, nodes: List = None, verges: List = None, **graph_data):
        self.nodes = nodes or []
        self.verges = verges or []
        self._graph_data = graph_data

    def create_node(self, verges: List = None, **node_data):
        node = Node(verges=verges, **node_data)
        self.nodes.append(node)
        return node

    def create_verge(self, node1: Node, node2: Node, **verge_data):
        verge = Verge(node1=node1, node2=node2, verge_data=verge_data)
        self.verges.append(verge)
        return verge

    def get_node_by_index(self, index: int):
        if index >= len(self.nodes):
            raise IndexError('Not found node with given index')
        return self.nodes[index]




