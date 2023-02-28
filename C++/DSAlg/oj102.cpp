#include <iostream>
using namespace std;

class Point
{
public:
    int x;
    int y;
};

int base[3001] = {0};
int maxsize;

void sqa10(int n, int base[])
{
    for (int i = 1; i <= maxsize; i++)
    {
        if (base[i] != 0)
        {
            for (int j = 0; j < n; j++)
            {
                cout << base[i] + j + n + 1 << ' ';
            }
        }
    }
    cout << '\n';
    for (int i = 1; i <= maxsize; i++)
    {
        if (base[i] != 0)
        {
            for (int j = 0; j < n; j++)
            {
                cout << base[i] + j << ' ';
            }
        }
    }
    cout << '\n';
}
void sqa11(int n, int base[])
{
    for (int i = 1; i <= maxsize; i++)
    {
        if (base[i] != 0)
        {
            for (int j = 0; j < n; j++)
            {
                cout << base[i] + j << ' ';
            }
        }
    }
    cout << '\n';
    for (int i = 1; i <= maxsize; i++)
    {
        if (base[i] != 0)
        {
            for (int j = 0; j < n; j++)
            {
                cout << base[i] + j + n << ' ';
            }
        }
    }
    cout << '\n';
}
void sqa2(int n, int base[])
{
    for (int i = 1; i <= maxsize; i++)
    {
        if (base[i] != 0)
        {
            for (int j = 0; j < n; j++)
            {
                cout << base[i] + j << ' ';
            }
        }
    }
    cout << '\n';
    for (int i = 1; i <= maxsize; i++)
    {
        if (base[i] != 0)
        {
            for (int j = 0; j < n; j++)
            {
                cout << base[i] + j + n + 1 << ' ';
            }
        }
    }
    cout << '\n';
}
void slide(int n, int x)
{
    cout << x + n << ' ';
    cout << '\n';
    for (int j = 0; j < n - 1; j++)
    {
        cout << x + j << ' ';
    }
    cout << '\n';

    for (int j = 0; j < n; j++)
    {
        cout << x + j << ' ';
    }

    cout << '\n';

    cout << x + n << ' ';

    cout << '\n';
}
void rec(int n, int base[])
{
    for (int i = 1; i <= maxsize; i++)
    {
        if (base[i] != 0)
        {
            for (int j = 0; j < n; j++)
            {
                cout << base[i] + j + n << ' ';
            }
        }
    }
    cout << '\n';
    for (int i = 1; i <= maxsize; i++)
    {
        if (base[i] != 0)
        {
            for (int j = 0; j < n - 1; j++)
            {
                cout << base[i] + j << ' ';
            }
        }
    }
    cout << '\n';
    for (int i = 1; i <= maxsize; i++)
    {
        if (base[i] != 0)
        {
            for (int j = 0; j < n - 1; j++)
            {
                cout << base[i] + j + n + 1 << ' ';
            }
        }
    }
    cout << '\n';
    for (int i = 1; i <= maxsize; i++)
    {
        if (base[i] != 0)
        {
            for (int j = 0; j < n; j++)
            {
                cout << base[i] + j << ' ';
            }
        }
    }
    cout << '\n';
}
void ten1(int n, Point point)
{
    for (int i = point.y - (n - 1) / 2; i <= point.y + n / 2; i++)
    {
        if (i != point.y && i != point.y + 1)
        {
            cout << i << ' ';
        }
    }
    cout << '\n'
         << point.x << '\n'
         << point.y << '\n';
    for (int i = point.x - (n - 1) / 2; i <= point.x + (n) / 2; i++)
    {
        if (i != point.x && i != point.x - 1)
        {
            cout << i << ' ';
        }
    }
    cout << '\n';
}
void ten2(int n, Point point)
{
    for (int i = point.y - (n - 1) / 2; i <= point.y + (n) / 2; i++)
    {
        if (i != point.y && i != point.y + 1)
        {
            cout << i - 1 << ' ';
        }
    }
    cout << '\n'
         << point.x - 1 << '\n'
         << point.y - 1 << '\n';
    for (int i = point.x - (n - 1) / 2; i <= point.x + (n) / 2; i++)
    {
        if (i != point.x && i != point.x - 1)
        {
            cout << i - 1 << ' ';
        }
    }
    cout << '\n';
}
void compute(int n, int base[])
{
    if (n % 2 == 0)
    {
        if (n == 2)
        {
            for (int i = 1; i <= maxsize; i++)
            {
                if (base[i] != 0)
                {
                    cout << base[i] << ' ';
                }
            }
            cout << '\n';
            for (int i = 1; i <= maxsize; i++)
            {
                if (base[i] != 0)
                {
                    cout << base[i] + 1 << ' ';
                }
            }
            cout << '\n';
        }
        else
        {
            if (n == 4)
            {
                for (int i = 1; i <= maxsize; i++)
                {
                    if (base[i] != 0)
                    {
                        cout << base[i] << ' ' << base[i] + 1 << ' ';
                    }
                }
                cout << '\n';
                for (int i = 1; i <= maxsize; i++)
                {
                    if (base[i] != 0)
                    {
                        cout << base[i] + 2 << ' ' << base[i] + 3 << ' ';
                    }
                }
                cout << '\n';
                for (int i = 1; i <= maxsize; i++)
                {
                    if (base[i] != 0)
                    {
                        cout << base[i] + 2 << ' ' << base[i] + 3 << ' ';
                    }
                }
                cout << '\n';
                for (int i = 1; i <= maxsize; i++)
                {
                    if (base[i] != 0)
                    {
                        cout << base[i] << ' ';
                    }
                }
                cout << '\n';
                for (int i = 1; i <= maxsize; i++)
                {
                    if (base[i] != 0)
                    {
                        cout << base[i] + 3 << ' ';
                    }
                }
                cout << '\n';
                for (int i = 1; i <= maxsize; i++)
                {
                    if (base[i] != 0)
                    {
                        cout << base[i] << ' ' << base[i] + 1 << ' ';
                    }
                }
                cout << '\n';
                for (int i = 1; i <= maxsize; i++)
                {
                    if (base[i] != 0)
                    {
                        cout << base[i] << ' ';
                    }
                }
                cout << '\n';
                for (int i = 1; i <= maxsize; i++)
                {
                    if (base[i] != 0)
                    {
                        cout << base[i] + 1 << ' ';
                    }
                }
                cout << '\n';
                for (int i = 1; i <= maxsize; i++)
                {
                    if (base[i] != 0)
                    {
                        cout << base[i] + 2 << ' ';
                    }
                }
                cout << '\n';
                for (int i = 1; i <= maxsize; i++)
                {
                    if (base[i] != 0)
                    {
                        cout << base[i] + 3 << ' ';
                    }
                }
                cout << '\n';
            }

            else
            {
                sqa11(n / 2, base);
                rec(n / 2, base);
                for (int i = 1; i <= maxsize; i++)
                {
                    if (base[i] != 0)
                    {
                        Point center;
                        center.x = base[i] + n / 2;
                        center.y = base[i] + n / 2;
                        ten2(n, center);
                    }
                }
                for (int i = 1; i <= maxsize; i++)
                {
                    if (base[i] != 0)
                    {
                        base[i + n / 2] = i + n / 2;
                    }
                }
                compute(n / 2 - 1, base);
                slide(n / 2 - 1, n / 2);
            }
        }
    }
    else
    {
        if (n == 3)
        {
            for (int i = 1; i <= maxsize; i++)
            {
                if (base[i] != 0)
                {
                    cout << base[i] << ' ';
                }
            }
            cout << '\n';
            for (int i = 1; i <= maxsize; i++)
            {
                if (base[i] != 0)
                {
                    cout << base[i] + 1 << ' ' << base[i] + 2 << ' ';
                }
            }
            cout << '\n';
            for (int i = 1; i <= maxsize; i++)
            {
                if (base[i] != 0)
                {
                    cout << base[i] + 2 << ' ';
                }
            }
            cout << '\n';
            for (int i = 1; i <= maxsize; i++)
            {
                if (base[i] != 0)
                {
                    cout << base[i] << ' ';
                }
            }
            cout << '\n';
            for (int i = 1; i <= maxsize; i++)
            {
                if (base[i] != 0)
                {
                    cout << base[i] + 1 << ' ';
                }
            }
            cout << '\n';
            for (int i = 1; i <= maxsize; i++)
            {
                if (base[i] != 0)
                {
                    cout << base[i] + 2 << ' ';
                }
            }
            cout << '\n';
        }
        else
        {
            sqa10((n - 1) / 2, base);
            sqa2((n - 1) / 2, base);
            for (int i = 1; i <= maxsize; i++)
            {
                if (base[i] != 0)
                {
                    Point center;
                    center.x = base[i] + n / 2;
                    center.y = base[i] + n / 2;
                    ten1(n, center);
                }
            }
            for (int i = 1; i <= maxsize; i++)
            {
                if (base[i] != 0)
                {
                    base[i + (n + 1) / 2] = i + (n + 1) / 2;
                }
            }
            compute((n - 1) / 2, base);
        }
    }
}

int main()
{
    int n;
    cin >> n;
    maxsize = n;
    base[1] = 1;
    compute(n, base);
    system("pause");
    return 0;
}