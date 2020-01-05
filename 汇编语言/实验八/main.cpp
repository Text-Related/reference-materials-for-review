#include <iostream>
#include "add.hpp"
using namespace std;

int main()
{
	int a=1;
	int b=5;
	int c=0;

	c = add(a, b);
	cout << "a=" << a << endl;
	cout << "b=" << b << endl;
	cout << "c=" << c << endl;
	return 0;
}
