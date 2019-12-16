import compas
from compas.datastructures import Mesh
from compas.datastructures import mesh_quads_to_triangles
from compas.geometry import Box

from compas_plotters import MeshPlotter
from compas_viewers.multimeshviewer import MultiMeshViewer
from compas.utilities import print_profile

mesh = Mesh.from_obj(compas.get('faces.obj'))
mesh = Mesh.from_shape(Box.from_corner_corner_height((0.0, 0.0, 0.0), (1.0, 1.0, 0.0), 1.0))

trimesh = mesh.copy()
mesh_quads_to_triangles(trimesh)

tri = print_profile(mesh_subdivide_tri)
quad = print_profile(mesh_subdivide_quad)
ck = print_profile(mesh_subdivide_catmullclark)
corner = print_profile(mesh_subdivide_corner)
doosabin = print_profile(mesh_subdivide_doosabin)
loop = print_profile(trimesh_subdivide_loop)

tri_subd = tri(mesh, k=3)
quad_subd = quad(mesh, k=3)
ck_subd = ck(mesh, k=3)
corner_subd = corner(mesh, k=3)
doosabin_subd = doosabin(mesh, k=3)
loop_subd = loop(trimesh, k=3)

print(tri_subd.number_of_faces())
print(quad_subd.number_of_faces())
print(ck_subd.number_of_faces())
print(corner_subd.number_of_faces())
print(doosabin_subd.number_of_faces())
print(loop_subd.number_of_faces())

viewer = MultiMeshViewer()



viewer.show()
