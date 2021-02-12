#include <iostream>
#include <cmath>
using namespace std;

int main(){
	int h, b, c, s;
	cin >> h >> b >> c >> s;
	printf("%.1lf MB", (double)h*b*c*s/pow(2,23));
	return 0;
}