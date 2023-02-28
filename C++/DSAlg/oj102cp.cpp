#include <iostream>
#include <set>
using namespace std;

class Point
{
public:
    int x;
    int y;
};

set<int> base;

void sqa(int n, Point point)
{
    for (int i = 0; i < n; i++)
    {
        cout << point.x + i << ' ';
    }
    cout << '\n';
    for (int i = 0; i < n; i++)
    {
        cout << point.y + i << ' ';
    }
    cout << '\n';
}

void rec(int n, Point point)
{
    for (int i = 0; i < n - 1; i++)
    {
        cout << point.x + i + 1 << ' ';
    }
    cout << '\n';
    for (int i = 0; i < n; i++)
    {
        cout << point.y + i << ' ';
    }
    cout << '\n';
    for (int i = 0; i < n; i++)
    {
        cout << point.x + i << ' ';
    }
    cout << '\n';
    for (int i = 0; i < n - 1; i++)
    {
        cout << point.y + i << ' ';
    }
    cout << '\n';
}
void ten(int n, Point point)
{
    for (int i = point.y - (n - 1) / 2; i <= point.y + (n) / 2; i++)
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

void compute(int n, set<int> *base)
{
    if (n % 2 == 0)
    {
        if (n == 2)
        {
            for (set<int>::iterator it = base.begin(); it != base.end(); it++)
            {
                cout << *it << ' ';
            }
            cout << '\n';
            for (set<int>::iterator it = base.begin(); it != base.end(); it++)
            {
                cout << *it + 1 << ' ';
            }
            cout << '\n';
        }
        else
        {
            Point rightup;
            rightup.x = point.x;
            rightup.y = point.y + n / 2;
            sqa(n / 2, rightup);
            Point leftdown;
            leftdown.x = point.x + n / 2;
            leftdown.y = point.y;
            rec(n / 2, leftdown);
            Point center;
            center.x = point.x + n / 2 - 1;
            center.y = point.y + n / 2 - 1;
            ten(n, center);
            compute(n / 2 - 1, &base);
        }
    }
    else
    {
        if (n == 3)
        {
            for (set<int>::iterator it = base.begin(); it != base.end(); it++)
            {
                cout << *it << ' ';
            }
            cout << '\n';
            for (set<int>::iterator it = base.begin(); it != base.end(); it++)
            {
                cout << *it + 1 << ' ' << *it + 2 << ' ';
            }
            cout << '\n';
            for (set<int>::iterator it = base.begin(); it != base.end(); it++)
            {
                cout << *it + 2 << ' ';
            }
            cout << '\n';
            for (set<int>::iterator it = base.begin(); it != base.end(); it++)
            {
                cout << *it << ' ';
            }
            cout << '\n';
            for (set<int>::iterator it = base.begin(); it != base.end(); it++)
            {
                cout << *it + 1 << ' ';
            }
            cout << '\n';
            for (set<int>::iterator it = base.begin(); it != base.end(); it++)
            {
                cout << *it + 2 << ' ';
            }
            cout << '\n';
        }
        else
        {
            Point rightup;
            rightup.x = point.x + (n + 1) / 2;
            rightup.y = point.y;
            sqa((n - 1) / 2, rightup);
            Point leftdown;
            leftdown.x = point.x;
            leftdown.y = point.y + (n + 1) / 2;
            sqa((n - 1) / 2, leftdown);
            Point center;
            center.x = point.x + (n - 1) / 2;
            center.y = point.y + (n - 1) / 2;
            ten(n, center);
            Point rightdown;
            rightdown.x = point.x + (n + 1) / 2;
            rightdown.y = point.y + (n + 1) / 2;
            compute((n - 1) / 2, point);
            compute((n - 1) / 2, rightdown);
        }
    }
}

int main()
{
    int n;
    cin >> n;
    Point origin;
    origin.x = 1;
    origin.y = 1;
    base.insert(1);
    compute(n, base);
    system("pause");
    return 0;
}