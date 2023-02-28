#include <iostream>
#include <algorithm>
#include <queue>

using namespace std;

typedef struct _MAXHEAP
{
    priority_queue<int> Q, D;
    void push(int x) { Q.push(x); }
    void erase(int x) { D.push(x); }
    bool empty()
    {
        return Q.empty();
    }
    int top()
    {
        while (!D.empty() && Q.top() == D.top())
        {
            Q.pop();
            D.pop();
        }
        return Q.empty() ? 0 : Q.top();
    }
} MAXHEAP;

typedef struct _MINHEAP
{
    priority_queue<int, vector<int>, greater<int>> Q, D;
    void push(int x) { Q.push(x); }
    void erase(int x) { D.push(x); }
    bool empty()
    {
        return Q.empty();
    }
    int top()
    {
        while (!D.empty() && Q.top() == D.top())
        {
            Q.pop();
            D.pop();
        }
        return Q.empty() ? 0 : Q.top();
    }
} MINHEAP;

void find(int a[], int n, int k)
{
    int sub[k];
    int mid;
    for (int i = 0; i < k; i++)
    {
        sub[i] = a[i];
    }
    sort(sub, sub + k);
    MAXHEAP max_heap;
    MINHEAP min_heap;
    for (int i = 0; i < k; i++)
    {
        if (i < (k - 1) / 2)
        {
            max_heap.push(sub[i]);
        }
        else if (i > (k - 1) / 2)
        {
            min_heap.push(sub[i]);
        }
    }
    mid = sub[(k - 1) / 2];
    cout << mid << ' ';
    bool limit = false;
    for (int i = k; i < n; i++)
    {
        if (i == n - 1)
        {
            limit = true;
        }

        if (a[i - k] > mid)
        {
            min_heap.erase(a[i - k]);
            if (a[i] > mid)
            {
                min_heap.push(a[i]);
            }
            else
            {
                min_heap.push(mid);
                max_heap.push(a[i]);
                mid = max_heap.top();
                max_heap.erase(max_heap.top());
            }
        }
        else if (a[i - k] < mid)
        {
            max_heap.erase(a[i - k]);
            if (a[i] < mid)
            {
                max_heap.push(a[i]);
            }
            else
            {
                max_heap.push(mid);
                min_heap.push(a[i]);
                mid = min_heap.top();
                min_heap.erase(min_heap.top());
            }
        }
        else
        {
            if (a[i] > mid)
            {
                min_heap.push(a[i]);
                mid = min_heap.top();
                min_heap.erase(min_heap.top());
            }
            else
            {
                max_heap.push(a[i]);
                mid = max_heap.top();
                max_heap.erase(max_heap.top());
            }
        }
        if (!limit)
        {
            cout << mid << ' ';
        }
        else
            cout << mid;
    }
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0), cout.tie(0);
    int n, k;
    cin >> n >> k;
    int a[n];
    for (int i = 0; i < n; i++)
    {
        cin >> a[i];
    }
    find(a, n, k);
    system("pause");
    return 0;
}