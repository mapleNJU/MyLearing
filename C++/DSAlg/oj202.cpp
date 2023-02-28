#include <iostream>
#include <string>
#include <algorithm>
#include <unordered_map>

using namespace std;

int main()
{
    /*
    ios::sync_with_stdio(false);
    cin.tie(0), cout.tie(0);
    */
    long long int n;
    cin >> n;
    string all[n];
    unordered_multimap<long long int, int> map;
    long long int total = 0;
    long long int ask[n] = {0};

    for (int i = 0; i < n; i++)
    {
        cin >> all[i];
        for (int j = 'a'; j < 'a' + 26; j++)
        {
            long long int num = count(all[i].begin(), all[i].end(), j);
            ask[i] += (1 << (j - 'a')) * (num & 1);
        }
        map.insert({ask[i], ask[i] & 1});
    }

    for (int i = 0; i < n; i++) //开始对每一个key检索
    {
        total = total + map.count(ask[i]) - 1; //相等情况

        for (int j = 0; j < 26; j++) //不想等,只有一位不同
        {                            //通过给ask[i]的每一二进制位取反来判断是否存在
            total += map.count(ask[i] ^ (1 << j));
        }
        /*
        map.erase(ask[i]);
        while (temp > 1)
        {
            map.insert({ask[i], ask[i] & 1});
            temp--;
        }
        */
    }
    cout << total / 2;
    system("pause");
    return 0;
}