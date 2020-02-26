from math import radians
from math import sqrt
import compas
from compas.datastructures import Mesh
from compas.geometry import Rotation
from compas.geometry import Translation
from compas.geometry import distance_point_point_xy
from compas_plotters import MeshPlotter

mesh = Mesh.from_polyhedron(6)

origin = [0.0, 0.0, 0.0]
corner = mesh.vertex_attributes(mesh.get_any_vertex(), 'xyz')

d = distance_point_point_xy(origin, corner)

R = Rotation.from_axis_and_angle([0.0, 0.0, 1.0], radians(45))
T = Translation([d, d, 0.0])
X = T * R

mesh.transform(X)

mesh.add_vertex(x=0.0, y=0.0)

plotter = MeshPlotter(mesh, figsize=(8, 5))

plotter.draw_vertices()
plotter.draw_edges()
plotter.draw_faces()

plotter.show()
