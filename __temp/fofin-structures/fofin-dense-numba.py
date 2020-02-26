from compas.numerical import drx_numba
from compas.datastructures import Network
from compas_viewers.vtkviewer import VtkViewer

m = 150
p = [(i / m - 0.5) * 5 for i in range(m + 1)]
nodes = [[xi, yi, 0] for yi in p for xi in p]
edges = []

for i in range(m):
    for j in range(m):

        s = (m + 1)
        p1 = (j + 0) * s + i + 0
        p2 = (j + 0) * s + i + 1
        p3 = (j + 1) * s + i + 0
        p4 = (j + 1) * s + i + 1

        edges.append([p1, p2])
        edges.append([p1, p3])

        if j == m - 1:
            edges.append([p4, p3])

        if i == m - 1:
            edges.append([p2, p4])

network = Network.from_nodes_and_edges(nodes, edges)
sides = [i for i in network.nodes() if network.degree(i) <= 2]
network.update_default_node_attributes({'P': [0, 0, 1000 / network.number_of_nodes()]})
network.update_default_edge_attributes({'E': 100, 'A': 1, 'ct': 't'})
network.nodes_attributes(keys=sides, names='B', values=[[0, 0, 0]])

drx_numba(network=network, tol=0.01, summary=1, update=1)

data = {
    'nodes': [network.node_coordinates(i) for i in network.nodes()],
    'edges': [{'nodes': uv} for uv in network.edges()]
}

viewer = VtkViewer(data=data)
# viewer.node_size = 0
viewer.setup()
viewer.start()
