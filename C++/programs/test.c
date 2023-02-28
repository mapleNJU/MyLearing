#include <stdio.h>
#include <stdint.h>

uint64_t mod(uint64_t a, uint64_t b)
{
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

int main()
{
    uint64_t a, b, m;
    uint x1, x2, x3, x4;
    x1 = x2 = x3 = x4 = 0;
    A = a & (-1UL << 32);
    B = a & (-1UL);
    C = b & (-1UL << 32);
    D = b & (-1UL);
    if (A != 0 && C != 0)
    {
        x1=mod(mul(mod(mul(A,C),m),mul(2,mod(1<<63,m)),m);
    }
    if (A != 0 && D != 0)
    {
        x2=mod(mul(mod(mul(A,D),m),mod(1<<32,m),m);
    }
    if (B != 0 && C != 0)
    {
        x3=mod(mul(mod(mul(B,C),m),mod(1<<32,m),m);
    }
    if (B != 0 && D != 0)
    {
        x4 = mod(mul(B, D), m);
    }
    result = mod((x1 + x2 + x3 + x4), m);
}