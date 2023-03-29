#include <iostream>
#include <vector>
using namespace std;

void rotate(const vector<vector<int>> &mat)
{
    int basic = 0;
    int sizem = mat.size();
    int border = sizem / 2;
    for (; basic < border; basic++)
    {
        }
}

int main()
{
    int raw, column;
    cin >> raw >> column;
    vector<vector<int>> mat(raw, vector<int>(column, 0)); // 初始化row*column二维动态数组，初始化值为0
    for (int i = 0; i < column * raw; i++)
    {
        cin >> mat[i / column][i % column];
    }
    rotate(mat);
    for (int i = 0; i < raw; i++)
    {
        for (int j = 0; j < column; j++)
        {
            cout << mat[i][j] << ' ';
        }
    }
    system("pause");
    return 0;
}