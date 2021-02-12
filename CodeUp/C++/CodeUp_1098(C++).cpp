#include <iostream>
using namespace std;

int main(){
	int h, w, n, l, d, x, y;
	int a[101][101]={};
	cin >> h >> w;
	cin >> n;
	for(int k=0; k<n; k++){
		cin >> l >> d >> x >> y;
		if(d==0)
			for(int j=y; j<y+l; j++)
				a[x][j]=1;
		else
			for(int i=x; i<x+l; i++)
				a[i][y]=1;
	}
	for(int i=1; i<=h; i++){
		for(int j=1; j<=w; j++)
			cout << a[i][j] << " ";
		cout << endl;	
	}
	return 0;
}