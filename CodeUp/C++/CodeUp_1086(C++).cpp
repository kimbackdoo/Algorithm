#include <iostream>
#include <cmath>
using namespace std;

int main(){
	int w, h, b;
	cin >> w >> h >> b;
	if((0<w&&w<=1024)&&(0<h&&h<=1024)&&(b%4==0&&b<=40))
		printf("%.2lf MB", (double)w*h*b/pow(2,23));
	else
		cout << "Error!" << endl;
	return 0;
}