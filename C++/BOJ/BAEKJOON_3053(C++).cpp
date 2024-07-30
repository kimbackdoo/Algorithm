#include <iostream>
#define _USE_MATH_DEFINES
#include <cmath>
using namespace std;

int main(){
	int r;
	cin >> r;
	printf("%.6lf \n", (double)pow(r,2)*M_PI);
	printf("%.6lf \n", (double)2*pow(r,2));
}