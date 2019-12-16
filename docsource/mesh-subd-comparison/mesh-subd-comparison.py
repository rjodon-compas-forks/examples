from functools import partial

import compas
from compas.datastructures import Mesh
from compas.datastructures import mesh_quads_to_triangles
from compas.datastructures import mesh_subdivide
from compas.datastructures import trimesh_subdivide_loop
from compas.datastructures import mesh_subdivide_frames
from compas.datastructures import mesh_transform
from compas.geometry import Box
from compas.geometry import Translation

from compas_plotters import MeshPlotter
from compas_viewers.multimeshviewer import MultiMeshViewer
from compas.utilities import print_profile

mesh = Mesh.from_obj(compas.get('faces.obj'))
mesh = Mesh.from_shape(Box.from_corner_corner_height((0.0, 0.0, 0.0), (1.0, 1.0, 0.0), 1.0))

trimesh = mesh.copy()
mesh_quads_to_triangles(trimesh)

tri = print_profile(partial(mesh_subdivide, scheme='tri'))
quad = print_profile(partial(mesh_subdivide, scheme='quad'))
ck = print_profile(partial(mesh_subdivide, scheme='catmullclark'))
corner = print_profile(partial(mesh_subdivide, scheme='corner'))
doosabin = print_profile(partial(mesh_subdivide, scheme='doosabin'))
loop = print_profile(trimesh_subdivide_loop)
frames = print_profile(mesh_subdivide_frames)

tri_mesh = tri(mesh, k=3)
quad_mesh = quad(mesh, k=3)
ck_mesh = ck(mesh, k=3)
corner_mesh = corner(mesh, k=3)
doosabin_mesh = doosabin(mesh, k=3)
loop_mesh = loop(trimesh, k=3)
frames_mesh = frames(mesh, 0.1)

mesh_transform(quad_mesh, Translation([1.2, 0.0, 0.0]))
mesh_transform(corner_mesh, Translation([1.2 * 2, 0.0, 0.0]))
mesh_transform(frames_mesh, Translation([1.2 * 3, 0.0, 0.0]))
mesh_transform(ck_mesh, Translation([1.2 * 4, 0.0, 0.0]))
mesh_transform(doosabin_mesh, Translation([1.2 * 5, 0.0, 0.0]))
mesh_transform(loop_mesh, Translation([1.2 * 6, 0.0, 0.0]))

print(tri_mesh.number_of_faces())
print(quad_mesh.number_of_faces())
print(ck_mesh.number_of_faces())
print(corner_mesh.number_of_faces())
print(doosabin_mesh.number_of_faces())
print(loop_mesh.number_of_faces())
print(frames_mesh.number_of_faces())

viewer = MultiMeshViewer()
viewer.meshes = [tri_mesh, quad_mesh, corner_mesh, frames_mesh, ck_mesh, doosabin_mesh, loop_mesh]
viewer.show()
