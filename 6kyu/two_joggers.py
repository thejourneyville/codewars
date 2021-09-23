def nbr_of_laps(x, y):
    prod = x * y

    x_lap = prod // x
    y_lap = prod // y

    return x_lap, y_lap


"""
#include <stdio.h>

typedef struct Laps_Pairing {
    int bob;
    int charles;
} laps;

laps nbr_of_laps(int x, int y) {
  int product = x * y;

  int count = 1;
  int x_lap = 0;
  int y_lap = 0;
  while (count <= product) {
    if (count % x == 0) {
      x_lap = count;
      break;
      }
    count++;
  }
  count = 1;
  while (count <= product) {
    if (count % y == 0) {
      y_lap = count;
      break;
    }
    count++;
  }

  struct Laps_Pairing results;

  results.bob = x_lap;
  results.charles = y_lap;
  return results;

}
"""