#include <cmath>
#include <iostream>
#include <numbers>

constexpr int N_DIMENSIONS_OF_SPHERES = 51;
constexpr int FIRST_DIMENSION_OF_SPHERE = 0;

constexpr int N_RADII = 21;
const double FIRST_RADIUS = 1.0;
const double RADII_INTERVAL = 0.05;

// https://en.wikipedia.org/wiki/N-sphere
// Calculate the volume of an n-sphere of radius 'r' in (n + 1)-dimensional
// Euclidean space, where "dimension = n" is the dimension of the n-sphere
// (not the dimension (n+1) of the Euclidean space which contains the n-sphere),
// and "radius = r" is the radius of the n-sphere.
double volume_n_sphere(double dimension, double radius) {
  dimension = (dimension + 1) / 2;
  return std::pow(std::numbers::pi * radius * radius, dimension) /
         std::tgamma(dimension + 1);
}

int protected_main([[maybe_unused]] int argc, [[maybe_unused]] char **argv) {
  for (int dimension = FIRST_DIMENSION_OF_SPHERE;
       dimension < N_DIMENSIONS_OF_SPHERES; ++dimension) {
    double radius = FIRST_RADIUS;
    for (int r_index = 0; r_index < N_RADII; ++r_index) {
      std::cout << dimension << " " << radius << " "
                << volume_n_sphere(dimension, radius) << '\n';
      radius += 0.05;
    }
  }
  return EXIT_SUCCESS;
}

int main([[maybe_unused]] int argc, [[maybe_unused]] char **argv) {
  try {
    return protected_main(argc, argv);
  } catch (const std::exception &e) {
    std::cerr << "Unhandled exception caught: " << e.what() << std::endl;
  } catch (...) {
    std::cerr << "Unknown exception caught." << std::endl;
  }
  return EXIT_FAILURE;
}