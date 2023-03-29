#include <iostream>
#include <vector>
using namespace std;

/*
0498
难度:中等
给你一个大小为 m x n 的矩阵 mat ，请以对角线遍历的顺序，用一个数组返回这个矩阵中的所有元素。
今天这题写的真艰难.
首先是对vector的应用,并不熟练,出了很多问题,幸好都纠正了,再者是对算法本身的理解,对边界情况考虑不充分,致使出现问题,导致数组超出边界,神奇的是它一会儿报segmentation fault,一会儿又不报,损失了很多机会.
*/

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
        if ((i == 0 && direction == -1) || (i == size_r - 1 && direction == 1))
        {
            if (j != size_c - 1)
            {
                j += 1;
                direction *= -1; // direction=1,右上到左下，direction=-1,左下到右上
                continue;
            }
            else
            {
                i += 1;
                direction *= -1;
                continue;
            }
        }
        if ((j == 0 && direction == 1) || (j == size_c - 1 && direction == -1))
        {
            if (i != size_r - 1)
            {
                i += 1;
                direction *= -1;
                continue;
            }
            else
            {
                j += 1;
                direction *= -1;
                continue;
            }
        }
        i = i + direction;
        j = j - direction;
    }
    return newarr;
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
    vector<int> array(raw * column);
    array = Digital(mat);
    for (int i = 0; i < column * raw; i++)
    {
        cout << array[i] << ' ';
    }
    system("pause");
    return 0;
}
