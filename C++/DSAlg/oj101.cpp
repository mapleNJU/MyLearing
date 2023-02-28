#include <queue>
#include <iostream>

using namespace std;

void medians(int a[], int n)
{
    int mid = a[0];
    cout << mid << ' ';
    priority_queue<int> q;
    priority_queue<int, vector<int>, greater<int>> p;
    bool limit = false;
    int count = 0;
    for (int i = 1; i < n; i++)
    {
        if (i == n - 1)
        {
            limit = true;
        }
        if (i % 2 != 0)
        {
            if (a[i] > mid)
            {
                p.push(a[i]);
                count = 1;
            }
            else
            {
                q.push(a[i]);
                count = -1;
            }
        }
        else
        {
            if ((count == -1 && a[i] > mid) || (count == 1 && a[i] < mid))
            {
                count > 0 ? q.push(a[i]) : p.push(a[i]);
            }
            else
            {
                if (count > 0)
                {
                    q.push(mid);
                    p.push(a[i]);
                    mid = p.top();
                    p.pop();
                }
                else
                {
                    p.push(mid);
                    q.push(a[i]);
                    mid = q.top();
                    q.pop();
                }
            }
            count = 0;
            if (!limit)
            {
                cout << mid << ' ';
            }
            else
                cout << mid;
        }
    }
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0), cout.tie(0);
    int n;
    cin >> n;
    int a[n];
    for (int i = 0; i < n; i++)
    {
        cin >> a[i];
    }
    medians(a, n);
    system("pause");
    return 0;
}