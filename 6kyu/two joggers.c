#include <stdio.h>

typedef struct Laps_Pairing {
    int bob;
    int charles;
} laps;

laps nbr_of_laps(int x, int y) {
  
  
  if (x == y) {
    struct Laps_Pairing results;
    results.bob = 1;
    results.charles = 1;
    return results;
  }

  int product = x * y;
  int max_x = product / x;
  int max_y = product / y;
  int divisor;

  if (max_x > max_y) {
    divisor = max_x - 1;
  }
  else {
    divisor = max_y - 1;
  }
  
  while (divisor > 1) {
    if (max_x % divisor == 0 && max_y % divisor == 0) {
      struct Laps_Pairing results;
      results.bob = max_x / divisor;
      results.charles = max_y / divisor;
      return results;
    }
    else {
      divisor--;
    }
  }
  
  struct Laps_Pairing results;
  results.bob = max_x;
  results.charles = max_y;
  return results;
  
}
