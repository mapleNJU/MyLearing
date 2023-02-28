#include <iostream>
#include <vector>
using namespace std;
void PlusOne(int a[], int n);

int main()
{
    /*心得：在leetcode提交时一直遇到heap-buffer-overflow
    屡次尝试无果，先将定义b[]的数组改用vector，仍无用
    最后发现是在计算数组a的size的时候，不能直接用sizeof(a)/sizeof(a[0]),直接调库
    n=a.size()即可。
    另外：在这里定义的时候最好还是写成vector<int> b(n+1)，否则依然会出现不能用变量定义数组的问题。
    */
    int n;
    cin >> n;
    int a[n];
    for (int i = 0; i < n; i++)
    {
        cin >> a[i];
    }
    PlusOne(a, n);
    system("pause");
}

void PlusOne(int a[], int n)
{
    for (int i = n - 1; i >= 0; i--)
    {
        if (a[i] == 9)
        {
            a[i] = 0;
            continue;
        }
        if (a[i] != 9)
        {
            a[i] += 1;
            break;
        }
    }
    if (a[0] == 0)
    {
        vector<int> b(n + 1);
        b[0] = 1;
        cout << "[";
        for (int i = 0; i < n; i++)
        {
            cout << b[i] << ",";
        }
        cout << b[n] << "]";
        return;
    }
    cout << "[";
    for (int i = 0; i < n - 1; i++)
    {
        cout << a[i] << ",";
    }
    cout << a[n - 1] << "]";
    return;
}