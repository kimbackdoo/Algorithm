#include <iostream>
using namespace std;

int main(){
	int n, xy[3][51]={};
	cin >> n;
	for(int i=0; i<n; i++)
		cin >> xy[0][i] >> xy[1][i];
	for(int i=0; i<n; i++)
		for(int j=0; j<n; j++){
			if(i==j) continue;
			if(xy[0][i]<xy[0][j]&&xy[1][i]<xy[1][j])
				xy[2][i]++;
		}
	for(int i=0; i<n; i++)
		cout << xy[2][i]+1 << " ";
	return 0;
}