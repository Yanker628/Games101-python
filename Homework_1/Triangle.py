import numpy as np


class Triangle:
    def __init__(self):
        self.v = np.zeros((3, 3))  # the original coordinates of the triangle, v0, v1, v2 in counterclockwise order
        # Per vertex values
        self.color = np.zeros((3, 3))  # color at each vertex
        self.tex_coords = np.zeros((3, 2))  # texture u, v
        self.normal = np.zeros((3, 3))  # normal vector for each vertex

    def a(self) -> np.array(3, ):
        return self.v[0]

    def b(self) -> np.array(3, ):
        return self.v[1]

    def c(self) -> np.array(3, ):
        return self.v[2]

    def set_vertex(self, ind: int, ver: np.array(3, )):  # set i-th vertex coordinates
        self.v[ind] = ver

    def set_normal(self, ind: int, n: np.array(3, )):  # set i-th vertex normal vector
        self.normal[ind] = n

    def set_color(self, ind: int, r: float, g: float, b: float):  # set i-th vertex color
        if (r < 0.0) | (r > 255.) | (g < 0.0) | (g > 255.) | (b < 0.0) | (b > 255.):
            raise Exception(r"Invalid color values!")
        self.color[ind] = np.array([r / 255., g / 255., b / 255.])

    def set_tex_coord(self, ind: int, s: float, t: float):
        self.tex_coords[ind] = np.array([s, t])

    def to_vector4(self) -> np.array(4, ):
        return np.hstack((self.v, np.array([1, 1, 1]).reshape(3, 1)))