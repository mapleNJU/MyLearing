#include <iostream>
#include <cstring>
using namespace std;

int main()
{
    string a;
    cin >> a;
    int re = 0;
    int l = a.size(); // 问题在于a.size()，不能用sizeof(a)/sizeof(a[0])来判断。
    cout << l;
    for (int i = 0; i < l; i++)
    {
        if (a[i] <= '9' && a[i] >= '0')
        {
            int num = int(a[i] - '0');
            if (re == 0)
            {
                re = num;
            }
            else
            {
                re = re * 10 + num;
            }
        }
        else
        {
            for (int j = re; j > 0; j--)
            {
                cout << a[i];
            }
            re = 0;
        }
    }
    system("pause");
}