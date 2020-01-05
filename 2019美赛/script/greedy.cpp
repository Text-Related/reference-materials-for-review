#include<iostream>
#include<vector>
#include<math.h>
#include<algorithm>
using namespace std;
vector<vector<int> > waitList(53, vector<int>(2)); //定义二维动态数组53行2列;


int main(void)
{
	int map[51][51];
	int w_size = 0;
	map[19][22] = 0;
	for (int j = 0;j < 51;j++)
	{
		for (int i = 0;i < 51;i++)
		{
			if ((j == 34 && (i >= 33 && i <= 37)) || (j == 35 && ((i >= 31 && i <= 33) || (i >= 27 && i <= 29))) || (j == 34 && ((i >= 29 && i <= 37) || (i == 27))) ||
				(j == 33 && (i == 26 || i == 27 || i == 31 || i == 30)) ||
				(j == 32 && (i == 26 || i == 30 || i == 29)) ||
				(j == 31 && (i >= 16 && i <= 26 || i == 29)) ||
				(j == 30 && (i == 16 || i == 28 || i == 29)) ||
				(j == 29 && i == 28) || (j == 28 && ((i >= 25 && i <= 28) || (i >= 19 && i <= 20))) || (j == 27 && (i >= 18 && i <= 25))
				)
			{
				map[i][j] = 1;
				waitList[w_size++][0] = i;
				waitList[w_size++][1] = j;
			}
			else map[i][j] = -1;
		}
	}
	
	for(int i=0; i< waitList.size(); i++)//输出二维动态数组 
    {
        for(int j=0;j<waitList[i].size();j++)
        {
            cout<<waitList[i][j]<<" ";
        }
        cout<<"\n";
    }
	return 0;
}
