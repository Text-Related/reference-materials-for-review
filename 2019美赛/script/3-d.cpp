#include<iostream>
#include<vector>

using namespace std;

 class CargoBay{
 	public:
 		int L, W, H;
 };
 
 class MED{
 	public:
 		int L, W, H;
 		int weight;
 };
 
int medDir[3][6][3] = {
	{{14, 7, 5}, {14, 5, 7}, {5, 14, 7}, {5, 7, 14}, {7, 5, 14}, {7, 14, 5}},
	{5, 8, 5}, {5, 5, 8}, {8, 5, 5}, {5, 8, 5}, {5, 5, 8}, {8, 5, 5},
	{12, 7, 4}, {12, 4, 7}, {4, 12, 7}, {4, 7, 12}, {7, 4, 12}, {7, 12, 4}
};
 
//��ʼ��λ��list
vector<int *> L;
L.push_back({0, 0, 0});
vector<int *> 
 
 //����ҩ������ͳ��Դ��������ط��õ�h w d 
 vector<int> tempDirection(int i, int medType)
 {
 	list<int> result;
 	result.assign(medDir[medType - 1][i], medDir[medType - 1][i] + 3);
 	return result;
 }
 
 //���ĳ��λ�ã������Ƿ�ɹ� 
 bool forEachPosition()
{
	return 0;
}
