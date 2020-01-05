#include <iostream>
#include <vector>
#include <math.h>
#include <algorithm>
#include <time.h>
#include <cstdlib>
#include <Windows.h>

using namespace std;

class drone {
public:
	int cur_x, cur_y;
	double rest_dis;
	bool over;
	vector<int> route;
};

int drone_num = 18;
drone fleet[18];
double farest = 52.6;
int dir[8][2] = { { -1, 0 },{ -1, 1 },{ 0, 1 },{ 1, 1 },{ 1, 0 },{ 1, -1 },{ 0, -1 },{ -1, -1 } }; 
int start[2] = { 19, 22 }; 
int map[51][51];
int alpha_return = 1;
vector<vector<int> > waitList; 


bool safe(int x, int y)
{
	if (x >= 0 && x <= 50 && y >= 0 && y <= 50)
		return true;
	else
		return false;
}

double judge_new(drone t, int x2, int y2)
{
	if (!safe(x2, y2)) return -2;
	bool can_return = 0;
	double dis = sqrt((t.cur_x - x2) * (t.cur_x - x2) + (t.cur_y - y2) * (t.cur_y - y2));
	if (t.rest_dis - dis - alpha_return >= sqrt((start[0] - x2) * (start[0] - x2) + (start[1] - y2) * (start[1] - y2))) can_return = 1;

	double weight = 0; 
	if (map[x2][y2] == 1)
		weight = 0.7;
	else if (map[x2][y2] == 0)
		weight = 0.16;
	else weight = 0.2;

	double v = 0;
	for (int i = 0;i < waitList.size();i++)
	{
		int m = waitList[i][0];
		int n = waitList[i][1];
		double d = sqrt((x2 - m) *(x2 - m) + (y2 - n) * (y2 - n));
		v = v + 1.0 / d;
	}
	if (can_return == 1) return weight * v;
	else return -1;
}

int best_move_dir(int map[51][51], drone t)
{
	int cur_x = t.cur_x;
	int cur_y = t.cur_y;
	vector<double> value;
	for (int i = 0;i < 8;i++)
	{
		int x2 = cur_x + dir[i][0];
		int y2 = cur_y + dir[i][1];
		double v = judge_new(t, x2, y2);
		value.push_back(v);
	}
	vector<double>::iterator max = max_element(begin(value), end(value));
	if (*max == -1) return -1;
	else
	{
		int max_dir = distance(begin(value), max);
		if (cur_y + dir[max_dir][1] < 22) return 2;
		else return max_dir;
	}
}

void move(int map[51][51], drone& t, int move_dir)
{
	int mx = dir[move_dir][0];
	int my = dir[move_dir][1];
	t.cur_x = t.cur_x + mx;
	t.cur_y = t.cur_y + my;
	if (map[t.cur_x][t.cur_y] == 1)
	{
		for (int i = 0;i < waitList.size();i++)
		{
			if (waitList[i][0] == t.cur_x && waitList[i][1] == t.cur_y)
			{
				waitList.erase(waitList.begin() + i);
				break;
			}
		}
	}
	map[t.cur_x][t.cur_y] = 0;
	double move_dis;
	if (mx * my == 0) move_dis = 1;
	else move_dis = sqrt(2);
	t.rest_dis = t.rest_dis - move_dis;
	t.route.push_back(move_dir);
}

double print_route(drone* fleet)
{
	double longest = 0;
	for (int i = 0;i < drone_num;i++)
	{
		if (farest - fleet[i].rest_dis > longest) 
			longest = farest - fleet[i].rest_dis;
		cout << "fleet " << i << ": ";
		for (int j = 0;j < fleet[i].route.size();j++)
			cout << fleet[i].route[j] << ", ";
		cout << "rest route: " << fleet[i].rest_dis;
		cout << endl;
	}
	return longest;
}

void initialize()
{
	for (int i = 0;i < drone_num;i++)
	{
		fleet[i].cur_x = 19;
		fleet[i].cur_y = 22;
		fleet[i].rest_dis = farest;
		fleet[i].over = 0;
	}

	map[15][32] = 1;
	map[16][32] = 1;
	map[17][32] = 1;
	map[18][32] = 1;
	map[20][32] = 1;
	map[14][33] = 1;
	map[18][33] = 1;
	map[19][33] = 1;
	map[14][34] = 1;
	map[18][34] = 1;
	map[19][34] = 1;
	map[19][35] = 1;
	map[14][35] = 1;
	map[18][34] = 1;
	map[15][36] = 1;
	map[16][36] = 1;
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
				) map[i][j] = 1;
			if (map[i][j] == 1)
			{
				vector<int> t;
				t.push_back(i);
				t.push_back(j);
				waitList.push_back(t);
			}
			else map[i][j] = -1;
		}
	}
}

int main(void)
{
	double aver = 0;
	initialize();
	for (int k = 0;k < 500;k++)
	{
		int rest_num = drone_num; 
		int iter = 0;
		while (rest_num != 0 && waitList.size() != 0)
		{
			Sleep(1000);
			srand((unsigned int)time(0));
			for (int i = 0;i < drone_num;i++)
			{
				if (!fleet[i].over)
				{
					if (fleet[i].route.size() < 2)
					{
						int dir;
						dir = rand() % (4 - 0 + 1);
						move(map, fleet[i], dir);
					}
					else
					{
						int move_dir = best_move_dir(map, fleet[i]);
						if (move_dir == -1) //结束探查，返回出发点 
						{
							fleet[i].over = 1;
							rest_num--;
							cout << "fleet " << i << " is run out of fuel." << endl;
						}
						else
							move(map, fleet[i], move_dir);
					}
				}
			}
			print_route(fleet);
			cout << waitList.size();
		}
		double longest = print_route(fleet);
		if(waitList.size() != 0) cout << "waitList:" << waitList.size() << endl;
		aver += double(longest / double(79.0 / 60));
	}
	cout << "average time:" << double(aver / 500.0) << endl;
	getchar();
	return 0;
}