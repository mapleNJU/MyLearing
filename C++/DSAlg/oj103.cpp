#include <iostream>
#include <algorithm>

using namespace std;

bool check(long long int a[], long long int b[], long long int mid, int n, long int k)
{
    int i = n - 1;
    int j = 0;
    long int num = 0;
    while (i >= 0 && j < n)
    {
        if (a[i] + b[j] <= mid)
        {
            num += i + 1;
            j++;
        }
        else
            i--;
    }
    return num >= k;
}

int find(long long int a[], long long int b[], int n, long int k)
{
    long long int min = a[0] + b[0];
    long long int max = a[n - 1] + b[n - 1];
    while (min < max)
    {
        long long int mid = min + (max - min) / 2;

        if (check(a, b, mid, n, k))
        {
            max = mid;
        }
        else
            min = mid + 1;
    }
    return min;
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0), cout.tie(0);
    int n;
    long int k;
    cin >> n >> k;
    long long int a[n];
    long long int b[n];
    for (int i = 0; i < n; i++)
    {
        cin >> a[i];
    }
    for (int i = 0; i < n; i++)
    {
        cin >> b[i];
    }
    long long int res = 0;
    sort(a, a + n);
    sort(b, b + n);
    if (k < n)
    {
        long long int s[k];
        long long int t[k];
        for (int i = 0; i < k; i++)
        {
            s[i] = a[i];
            t[i] = b[i];
        }
        res = find(s, t, k, k);
    }
    else
        res = find(a, b, n, k);
    cout << res;
    system("pause");
    return 0;
}