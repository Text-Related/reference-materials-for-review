#include <iostream>
#include <iomanip>
#include "add128.h"
using namespace std;
#define MYCOUT(x) cout << setbase(16) << setw(8) << setfill('0') << (x);
void printint128(int128 x)
{
	MYCOUT(x.l3);
	MYCOUT(x.l2);
	MYCOUT(x.l1);
	MYCOUT(x.l0);

	return;
}
int main()
{
	int128 a = {1,0,0,0};
	int128 b = {2,0,0,0};
	int128 c;

	add128(a,b,c);

	printint128(c);

	return 0;
}