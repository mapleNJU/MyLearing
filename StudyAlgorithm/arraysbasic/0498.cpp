#include <iostream>
#include <vector>
using namespace std;

vector<int> Digital(const vector<vector<int>> &mat)
{
    int size_r = mat.size();
    int size_c = mat[0].size();
    int direction = -1;
    int i = 0;
    int j = 0;
    vector<int> newarr(size_r * size_c); // 定义这里的时候别加等号！血泪教训
    for (int k = 0; k < size_r * size_c; k++)
    {
        newarr[k] = mat[i][j];
        if (i == 0 || j == 0)
        {
            if (i == 0 && direction == -1)
            {
                i -= 1;
                j += 2;
            }
            else if ((j == 0 || i == size_r - 1) && direction == 1 && i != 0)
            {
                j -= 1;
                i += 2;
            }
            direction *= -1; // direction=1代表从右上到左下，=-1代表从左下到右上
        }
        i += 1 * direction;
        j -= 1 * direction;
    }
    return newarr;
}

int main()
{
    int raw, column;
    cin >> raw >> column;
    vector<vector<int>> mat(raw, vector<int>(column, 0)); // 初始化row*column二维动态数组，初始化值为0
    vector<int> array(raw * column);
    array = Digital(mat);
    for (int i = 0; i < column * raw - 1; i++)
    {
        cout << array[i] << ' ';
    }
    cout << array[column * raw];
    system("pause");
    return 0;
}
