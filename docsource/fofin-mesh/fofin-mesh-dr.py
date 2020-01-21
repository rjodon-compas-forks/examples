import compas
from compas.datastructures import Mesh
from compas.numerical import dr_numpy

mesh = Mesh.from_obj(compas.get('faces.obj'))

mesh.update_default_vertex_attributes(is_anchor=False, px=0.0, py=0.0, pz=0.0, rx=0.0, ry=0.0, rz=0.0)
mesh.update_default_edge_attributes(q=0.0, f=0.0, l=0.0, qpre=1.0, fpre=0.0, lpre=0.0, l0=0.0, E=0.0, radius=0.0)

corners = list(mesh.vertices_where({'vertex_degree': 2}))
mesh.set_vertices_attribute('is_anchor', True, keys=corners)

key_index = mesh.key_index()
xyz = mesh.get_vertices_attributes('xyz')
loads = mesh.get_vertices_attributes(('px', 'py', 'pz'))
fixed = [key_index[key] for key in mesh.vertices_where({'is_anchor': True})]
edges = [(key_index[u], key_index[v]) for u, v in mesh.edges()]
qpre = mesh.get_edges_attribute('qpre')
fpre = mesh.get_edges_attribute('fpre')
lpre = mesh.get_edges_attribute('lpre')
linit = mesh.get_edges_attribute('l0')
E = mesh.get_edges_attribute('E')
radius = mesh.get_edges_attribute('radius')

xyz, q, f, l, r = dr_numpy(xyz, edges, fixed, loads, qpre, fpre, lpre, linit, E, radius)

for key, attr in mesh.vertices(True):
    index = key_index[key]
    mesh.set_vertex_attributes(key, 'xyz', xyz[index])
    mesh.set_vertex_attributes(key, ['rx', 'ry', 'rz'], r[index])
 
for index, (u, v, attr) in enumerate(mesh.edges(True)):
    attr['q'] = q[index, 0]
    attr['f'] = f[index, 0]
    attr['l'] = l[index, 0]
    