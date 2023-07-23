import json
import numpy as np
from objects.sphere import Sphere
from objects.scene import Scene


def compute_normal(point, sphere_center):
    """
    Compute the normal vector of the sphere at the intersection point
    """
    normal = point - sphere_center
    normal = normal / np.linalg.norm(normal)  # Normalize the vector
    return normal


def normalize(vec):
    """
    Normalize the vector
    """
    return vec / np.linalg.norm(vec)


def get_len_vec(vec):
    """
    Get the length of the vector
    """
    return np.linalg.norm(vec)


def load_scene(filename):
    """
    Load the scene from a JSON file
    """
    with open(filename, 'r') as f:
        data = json.load(f)
    spheres = [
        Sphere(
            np.array([s['center']['x'], s['center']['y'], s['center']['z']]),
            s['radius'],
            np.array([s['color']['x'], s['color']['y'], s['color']['z']]),
        )
        for s in data['spheres']
    ]
    return Scene(spheres)


def new_load_scene(filename):
    with open(filename, 'r') as f:
        data = json.load(f)

    return data