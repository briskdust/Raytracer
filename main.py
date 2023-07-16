import matplotlib.pyplot as plt

from objects.ray import Ray
from objects.light import Light

from functions.phong_shading import *


# Load the scenes from a JSON file
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

# Normalize the pixel values to [0, 1]
pixels = pixels / np.max(pixels)

plt.imsave('render.png', pixels)
