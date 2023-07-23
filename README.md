# Python Raytracer

<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-this-project">About This Project</a>
    </li>
    <li>
      <a href="#built-with">Built With</a>
    </li>
    <li>
      <a href="#scope">Scope</a>
    </li>
    <li>
        <a href="#getting-started">Getting Started</a>
    </li>
    <li>
        <a href="#future-improvements">Future Improvements</a>
    </li>
    <li>
        <a href="#credits">Credits</a>
    </li>
    <li>
        <a href="#license">License</a>
    </li>
  </ol>
</details>

## About This Project

This is a basic, yet effective, implementation of a raytracing renderer in Python. It uses basic light modeling, shadowing, and reflections to generate realistic renders of 3D scenes with spheres.

## Built With

* ![Python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)
* ![NumPy](https://img.shields.io/badge/Numpy-777BB4?style=for-the-badge&logo=numpy&logoColor=white)
* ![Matplotlib](https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black)
## Scope

- Basic sphere objects
- Ray-sphere intersection
- Simple Phong lighting model (ambient, diffuse, and specular)
- Loading scene from JSON file

## Getting Started

First, set up the scene you want to render. This is done through a JSON file. The JSON file should contain a list of sphere objects, each defined by its center, radius, and color. Here's an example:

```json
{
  "spheres": [
    {
      "center": {"x": 0, "y": 0, "z": 5},
      "radius": 1,
      "color": [255, 0, 0]
    },
    {
      "center": {"x": 2, "y": 0, "z": 5},
      "radius": 1,
      "color": [0, 255, 0]
    }
  ]
}
```

Then, run the raytracer with the path to your scene JSON:

```sh
python raytracer.py my_scene.json
```
| :exclamation: Note: Make sure to put all the scenes under `scenes/`. |
|----------------------------------------------------------------------|

This will render the scene and save the result as an image.

The position of the camera and light are currently fixed, but could easily be made configurable.

## Future Improvements

- Support for more types of objects (planes, cubes, etc.)
- More sophisticated lighting models
- Refraction, texture mapping, and other advanced raytracing features

## Credits

This project was created as part of learning and exploring the raytracing algorithm. It was implemented in Python due to its simplicity and rich set of libraries.

Feel free to use and modify the code for your own purposes. If you do something interesting with it, I'd love to hear about it!

## License

This project is licensed under the terms of the MIT license.
