#include <iostream>
using namespace std;
void q_sort(int *a, int l, int r)
{
    if (l < r)
    {
        int i = l;
        int j = r;
        int x = a[i];
        while (i < j)
        {
            while (i < j && a[j] >= x)
            {
                j--;
            }
            if (i < j)
            {
                a[i] = a[j];
            }
            while (i < j && a[i] < x)
            {
                i++;
            }
            if (i < j)
            {
                a[j] = a[i];
            }
        }
        a[i] = x;
        q_sort(a, l, i - 1);
        q_sort(a, i + 1, r);
    }
}
int main()
{
    int n;
    cin >> n;
    int a[n];
    for (int i = 0; i < n; i++)
    {
        cin >> a[i];
    }
    int mid = sizeof(a) / sizeof(a[0]) / 2;

    q_sort(a, 0, n);
    cout << a[mid];

    return 0;
}
