from numpy import linspace
from numpy import sign

from compas.datastructures import Network
from compas.numerical import drx_numpy 
from compas_plotters import NetworkPlotter

L = 2.5
n = 100
EI = 0.2

vertices = [[i, 1 - abs(i), 0] for i in list(linspace(-1, 1, n))]
for i in range(n):
    if vertices[i][1] < 0.5:
        vertices[i][0] = sign(vertices[i][0]) * vertices[i][1]
edges = [[i, i + 1] for i in range(n - 1)]

structure = Network.from_vertices_and_edges(vertices=vertices, edges=edges)
structure.update_default_vertex_attributes({'is_fixed': False, 'EIx': EI, 'EIy': EI})
structure.update_default_edge_attributes({'E': 50, 'A': 1, 'l0': L / n})
structure.set_vertices_attributes(['B', 'is_fixed'], [[0, 0, 0], True], structure.leaves())
structure.attributes['beams'] = {'beam': {'nodes': list(range(n))}}

lines = []
for u, v in structure.edges():
    lines.append({
        'start': structure.vertex_coordinates(u, 'xy'),
        'end': structure.vertex_coordinates(v, 'xy'),
        'color': '#cccccc'
    })

plotter = NetworkPlotter(structure, figsize=(8, 5))
plotter.draw_vertices(radius=0.005, facecolor={i: '#ff0000' for i in structure.vertices_where({'is_fixed': True})})
plotter.draw_lines(lines)
plotter.draw_edges()

def callback(X, k_i):

    for key in structure.vertices():
        x, y, z = X[k_i[key], :]
        structure.set_vertex_attributes(key, 'xyz', [x, y, z])
    plotter.update_edges()
    plotter.update(pause=0.01)

drx_numpy(structure=structure, tol=0.01, refresh=20, factor=30, update=1, callback=callback, k_i=structure.key_index())

plotter.show()
