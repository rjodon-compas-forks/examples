from compas.datastructures import Network
from compas_viewers import VtkViewer

m = 70
p = [(i / m - 0.5) * 5 for i in range(m + 1)]
vertices = [[xi, yi, 0] for yi in p for xi in p]
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

structure = Network.from_vertices_and_edges(vertices=vertices, edges=edges)
sides = [i for i in structure.vertices() if structure.vertex_degree(i) <= 2]
structure.update_default_vertex_attributes({'P': [0, 0, 1000 / structure.number_of_vertices()]})
structure.update_default_edge_attributes({'E': 100, 'A': 1, 'ct': 't'})
structure.vertices_attributes(keys=sides, names='B', values=[[0, 0, 0]])

data = {
    'vertices': [structure.vertex_coordinates(i) for i in structure.vertices()],
    'edges':    [{'vertices': uv} for uv in structure.edges()]
}

def callback(X, self):
    self.update_vertices_coordinates({i: X[i, :] for i in range(X.shape[0])})

def func(self):
    drx_numpy(structure=structure, tol=0.05, update=True, refresh=5, callback=callback, self=self)

print('Press key S to start')

viewer = VtkViewer(data=data)
viewer.vertex_size = 1
viewer.edge_width  = 10
viewer.keycallbacks['s'] = func
viewer.setup()
viewer.start()
