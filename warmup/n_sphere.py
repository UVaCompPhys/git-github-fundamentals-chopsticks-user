from math import pi, gamma, pow
import matplotlib.pyplot as plt
import numpy as np

N_DIMENSIONS_OF_SPHERES = 51
FIRST_DIMENSION_OF_SPHERE = 0

N_RADII = 21
FIRST_RADIUS = 1.0
LAST_RADIUS = 2.0
RADII_INTERVAL = 0.05


# https://en.wikipedia.org/wiki/N-sphere
# Calculate the volume of an n-sphere of radius 'r' in (n + 1)-dimensional
# Euclidean space, where "dimension = n" is the dimension of the n-sphere
# (not the dimension (n+1) of the Euclidean space which contains the n-sphere), and
# "radius = r" is the radius of the n-sphere.
def volume_n_sphere(dimension, radius):
    dimension = (dimension + 1) / 2
    return pow(pi * (radius**2), dimension) / gamma(dimension + 1)


def plot_volumes_3d(volumes):
    fig = plt.figure(figsize=(10, 7))
    ax = plt.axes(projection="3d")
    ax.set_xlabel("Dimension")
    ax.set_ylabel("Radius")
    ax.set_zlabel("Volume")
    plt.title("V(n, R), where n ∈ [0,50] and R ∈ [1.0, 2.0]")

    x = np.zeros(N_DIMENSIONS_OF_SPHERES*N_RADII, int)
    for i in range(N_DIMENSIONS_OF_SPHERES):
        for j in range(N_RADII):
            np.put(x, i*N_RADII+j, i)

    y = np.zeros(N_DIMENSIONS_OF_SPHERES*N_RADII, float)
    for i in range(N_DIMENSIONS_OF_SPHERES):
        for j in range(N_RADII):
            np.put(y, i*N_RADII+j, 1.0+j*0.05)

    z = volumes

    ax.scatter3D(x, y, z, color="blue")
    plt.show()


def plot_volumes_in_dimensions_2d(volumes, radius_fixed):
    fig = plt.figure(figsize=(10, 7))
    ax = plt.axes()
    ax.plot()
    ax.set_xlabel("Dimension")
    ax.set_ylabel("Volume")
    plt.title(
        f"V(n, R={radius_fixed}), where n ∈ [{FIRST_DIMENSION_OF_SPHERE},{N_DIMENSIONS_OF_SPHERES-1}]")

    x = np.zeros(N_DIMENSIONS_OF_SPHERES, int)
    np.put(x, np.arange(N_DIMENSIONS_OF_SPHERES),
           np.arange(N_DIMENSIONS_OF_SPHERES))

    y = np.zeros(N_DIMENSIONS_OF_SPHERES, float)
    i_radius = round((radius_fixed - FIRST_RADIUS) / RADII_INTERVAL)
    for i_y in range(N_DIMENSIONS_OF_SPHERES):
        y[i_y] = volumes[i_y][i_radius]
        i_y += 1

    ax.plot(x, y, "o-")
    ax.grid(True)
    plt.show()


def plot_volumes_of_radii_2d(volumes, dimension_fixed):
    fig = plt.figure(figsize=(10, 7))
    ax = plt.axes()
    ax.plot()
    ax.set_xlabel("Radius")
    ax.set_ylabel("Volume")
    plt.title(
        f"V({dimension_fixed}, R), where R ∈ [{FIRST_RADIUS},{LAST_RADIUS}]")

    x = np.zeros(N_RADII, float)
    np.put(x, np.arange(N_RADII),
           np.arange(FIRST_RADIUS, LAST_RADIUS+RADII_INTERVAL, RADII_INTERVAL))

    y = np.zeros(N_RADII, float)
    i_dim = round((dimension_fixed - FIRST_DIMENSION_OF_SPHERE))
    for i_y in range(N_RADII):
        y[i_y] = volumes[i_dim][i_y]
        i_y += 1

    ax.plot(x, y, "o-")
    ax.grid(True)
    plt.show()


if __name__ == '__main__':
    volumes = np.zeros((N_DIMENSIONS_OF_SPHERES, N_RADII), dtype=float)

    for dimension in range(N_DIMENSIONS_OF_SPHERES):
        radius = FIRST_RADIUS
        for i_radius in range(N_RADII):
            volumes[dimension][i_radius] = volume_n_sphere(dimension, radius)
            print(f"{dimension} {radius} {volumes[dimension][i_radius]}")
            radius += RADII_INTERVAL

    plot_volumes_3d(volumes)
