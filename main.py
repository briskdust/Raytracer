import json
import numpy as np
import matplotlib.pyplot as plt

from objects import sphere, ray
from config import *


class Sphere:
    def __init__(self, center, radius, color):
        self.center = center
        self.radius = radius
        self.color = color


class Ray:
    def __init__(self, origin, direction):
        self.origin = origin
        self.direction = direction


class Light:
    def __init__(self, position, intensity=1):
        self.position = position
        self.intensity = intensity


class Scene:
    def __init__(self, spheres):
        self.spheres = spheres


def compute_normal(point, sphere_center):
    normal = point - sphere_center
    normal = normal / np.linalg.norm(normal)  # Normalize the vector
    return normal


def normalize(vec):
    return vec / np.linalg.norm(vec)


def get_len_vec(vec):
    return np.linalg.norm(vec)


def load_scene(filename):
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


def ray_sphere_intersect(ray, sphere):
    oc = sphere.center - ray.origin
    a = np.dot(oc, normalize(ray.direction))
    dis_squared = np.dot(oc, oc) - a * a

    if dis_squared > sphere.radius * sphere.radius:
        return False
    else:
        distance = a - np.sqrt(sphere.radius ** 2 - dis_squared)
        intersection = ray.origin + ray.direction * distance
        return intersection


def compute_lighting(ray, light, sphere, point):
    ambient = ka * light.intensity

    light_dir = normalize((light.position - point))
    normal = compute_normal(point, sphere.center)
    diffuse = kd * light.intensity * max(0, np.dot(normal, light_dir))

    reflection_dir = normalize(2 * np.dot(light_dir, normal) * normal - light_dir)

    view_dir = normalize(ray.origin - point)

    specular = ks * light.intensity * max(0, np.dot(reflection_dir, view_dir)) ** 16

    return ambient + diffuse + specular


def trace_ray(ray, scene, light, depth=0):
    color = np.zeros(3)
    distance = float('inf')
    for sphere in scene.spheres:
        intersection = ray_sphere_intersect(ray, sphere)
        if intersection is not False:
            if get_len_vec(intersection - ray.origin) < distance:
                distance = get_len_vec(intersection - ray.origin)
                point = intersection
                sphere_intersected = sphere

    if distance < float('inf'):
        lighting = compute_lighting(ray, light, sphere_intersected, point)
        color += np.array(sphere_intersected.color) * lighting

    return color


# Load your scene from a JSON file
scene = load_scene('scenes/trial.json')

# Render the scene
width, height = 800, 800
camera = np.array([0, 0, 0])
pixels = np.zeros([height, width, 3])
light = Light(np.array([5, 5, 5]), 2)
for i in range(height):
    for j in range(width):
        direction = np.array([j / width - 0.5, i / height - 0.5, 1])
        ray = Ray(camera, direction)
        pixels[i, j] = trace_ray(ray, scene, light)

print(np.max(pixels))
# Normalize the pixel values to [0, 1]
pixels = pixels / np.max(pixels)

plt.imsave('render.png', pixels)
