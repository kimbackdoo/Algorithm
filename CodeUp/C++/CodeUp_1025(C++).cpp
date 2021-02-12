#include<iostream>
#include<cmath>
using namespace std;

int main(){
	int j=4;
	int a[5];
	scanf("%1d%1d%1d%1d%1d", &a[0], &a[1], &a[2], &a[3], &a[4]);
	for(int i=0; i<5; i++){
		cout << "[" << a[i]*pow(10,j) << "]" << endl;
		j--;
	}
	return 0;
}