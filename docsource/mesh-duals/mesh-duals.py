from functools import partial

from compas.datastructures import Mesh
from compas.datastructures import mesh_subdivide
from compas.datastructures import mesh_transform
from compas.datastructures import mesh_dual
from compas.geometry import Box
from compas.geometry import Translation
from compas.geometry import bounding_box_xy
from compas.geometry import distance_point_point
from compas_viewers.multimeshviewer import MultiMeshViewer

tri = partial(mesh_subdivide, scheme='tri')
quad = partial(mesh_subdivide, scheme='quad')
ck = partial(mesh_subdivide, scheme='catmullclark')
corner = partial(mesh_subdivide, scheme='corner')
doosabin = partial(mesh_subdivide, scheme='doosabin')


box = Box.from_corner_corner_height((0.0, 0.0, 0.0), (1.0, 1.0, 0.0), 1.0)
mesh = Mesh.from_shape(box)

bbox = bounding_box_xy(mesh.vertices_attributes('xyz'))
d = distance_point_point(bbox[0], bbox[1])

k = 2

tri_mesh = tri(mesh, k=k)
quad_mesh = quad(mesh, k=k)
ck_mesh = ck(mesh, k=k)
corner_mesh = corner(mesh, k=k)
doosabin_mesh = doosabin(mesh, k=k)

mesh_transform(quad_mesh, Translation([1.5 * d, 0.0, 0.0]))
mesh_transform(corner_mesh, Translation([1.5 * 2 * d, 0.0, 0.0]))
mesh_transform(ck_mesh, Translation([1.5 * 3 * d, 0.0, 0.0]))
mesh_transform(doosabin_mesh, Translation([1.5 * 4 * d, 0.0, 0.0]))

meshes = [tri_mesh, quad_mesh, corner_mesh, ck_mesh, doosabin_mesh]
duals = []
for mesh in meshes:
    dual = mesh_dual(mesh)
    duals.append(dual)
    mesh_transform(dual, Translation([0.0, 2.0 * d, 0.0]))

viewer = MultiMeshViewer()
viewer.meshes = meshes + duals
viewer.show()
