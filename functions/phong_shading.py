from functions.utils import *
from config import *


def ray_sphere_intersect(ray, sphere):
    """
    Compute the intersection point between the ray and the sphere
    :param ray: The ray to be intersected
    :param sphere: The sphere to be intersected
    :return: The intersection point if the ray intersects the sphere, False otherwise
    """
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
    """
    Compute the lighting of the sphere
    :param ray: The ray to be intersected
    :param light: The light source
    :param sphere: The sphere to be intersected
    :param point: The intersection point
    :return: THe lighting of the sphere
    """
    ambient = ka * light.intensity

    light_dir = normalize((light.position - point))
    normal = compute_normal(point, sphere.center)
    diffuse = kd * light.intensity * max(0, np.dot(normal, light_dir))

    reflection_dir = normalize(2 * np.dot(light_dir, normal) * normal - light_dir)

    view_dir = normalize(ray.origin - point)

    specular = ks * light.intensity * max(0, np.dot(reflection_dir, view_dir)) ** 16

    return ambient + diffuse + specular


def trace_ray(ray, scene, light):
    """
    Trace the ray and compute the color of the pixel
    :param ray: The ray to be traced
    :param scene: The scene to be traced
    :param light: The light source
    :return: The color of the pixel
    """
    color = np.zeros(3)
    distance = float('INF')
    for sphere in scene.spheres:
        intersection = ray_sphere_intersect(ray, sphere)
        if intersection is not False:
            if get_len_vec(intersection - ray.origin) < distance:
                distance = get_len_vec(intersection - ray.origin)
                point = intersection
                sphere_intersected = sphere

    if distance < float('INF'):
        lighting = compute_lighting(ray, light, sphere_intersected, point)
        color += np.array(sphere_intersected.color) * lighting

    return color
