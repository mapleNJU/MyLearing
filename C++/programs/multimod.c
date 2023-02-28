
#define __STDC_FORMAT_MACROS 1
#define U64 "%" PRIu64

#include <stdint.h>
#include <stdio.h>
#include <inttypes.h>
#include <stdlib.h>

uint64_t mul(uint64_t a, uint64_t b)
{
  int i = 0;
  uint64_t x = 0;
  while ((b | 0) != 0)
  {
    if ((b & 1) == 1)
    {
      x = x + (a << i);
    }
    i++;
    b = (b >> 1);
  }
  return x;
}

uint64_t mod(uint64_t a, uint64_t b)
{
  if (a < b)
  {
    return a;
  }
  uint64_t q = 0;
  for (int i = 63; i >= 0; i--)
  {
    if ((a >> i) >= b)
    {
      q = q + (q << i);
      a = a - (b << i);
    }
  }
  return a;
}
uint64_t summod(uint64_t a, uint64_t b, uint64_t m)
{
  if (a == 0 || b == 0)
  {
    return a == 0 ? b : a;
  }
  uint64_t sum = a + b;

  if (sum <= a || sum <= b)
  {
    return a - (m - b);
  }
  while (sum >= m)
  {
    sum = sum - m;
  }
  return sum;
}

uint64_t add(uint64_t a, uint64_t b, uint64_t m)
{
  uint64_t r = mod(b, m); // s0
  uint64_t result = 0;
  while (a)
  {
    if ((a & 1) == 1)
    {
      result += mod(r, m);
      printf(U64, result);
      printf("\n");
      result = mod(result, m);
    }
    r = summod(r, r, m);
    a = (a >> 1);
  }
  return result;
}
uint64_t multimod(uint64_t a, uint64_t b, uint64_t m)
{
  uint64_t x, y, z;
  x = y = z = 0;
  x = a;
  y = b;
  uint64_t sum = 0;
  sum = add(x, y, m);
  return sum;
}
// void test(uint64_t a, uint64_t b, uint64_t m)
//{

// printf(U64 " * " U64 " mod " U64 " = " U64 "\n", a, b, m, multimod(a, b, m));
// }
int main()
{

  uint64_t a, b, m;
  scanf(U64 U64 U64, &a, &b, &m);
  printf(U64 " * " U64 " mod " U64 " = " U64 "\n", a, b, m, multimod(a, b, m));
  // test(123, 456, -1ULL);
  // test(-2ULL, -2ULL, -1ULL);
  system("pause");
  return 0;
}
