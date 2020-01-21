import compas

from compas.datastructures import Network
from compas_plotters import NetworkPlotter

structure = Network.from_obj(compas.get('lines.obj'))
structure.update_default_vertex_attributes({'is_fixed': False, 'P': [1, 1, 0]})
structure.update_default_edge_attributes({'E': 10, 'A': 1, 'ct': 't'})
structure.set_vertices_attributes(['is_fixed', 'B'], [True, [0, 0, 0]], structure.leaves())

lines = []
for u, v in structure.edges():
    lines.append({
        'start': structure.vertex_coordinates(u, 'xy'),
        'end':   structure.vertex_coordinates(v, 'xy'),
        'color': '#cccccc'
    })

plotter = NetworkPlotter(structure, figsize=(10, 7))
plotter.draw_vertices(facecolor={key: '#ff0000' for key in structure.vertices_where({'is_fixed': True})})
plotter.draw_lines(lines)
plotter.draw_edges()

def callback(X, k_i):

    for key in structure.vertices():
        x, y, z = X[k_i[key], :]
        structure.set_vertex_attributes(key, 'xyz', [x, y, z])
    plotter.update_edges()
    plotter.update(pause=0.01)

drx_numpy(structure=structure, tol=0.001, refresh=1, update=True, callback=callback, k_i=structure.key_index())

plotter.show()
