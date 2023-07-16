import numpy as np


class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.vec = np.array([x, y, z])

    def normalize(self):
        return Vector(*self.vec / np.linalg.norm(self.vec))

    def length(self):
        return np.linalg.norm(self.vec)

    def get_vec(self):
        return self.vec
