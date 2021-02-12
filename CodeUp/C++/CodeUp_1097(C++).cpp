#include <iostream>
using namespace std;

int main(){
	int n, x, y;
	int a[20][20]={};
	for(int i=1; i<=19; i++)
		for(int j=1; j<=19; j++)
			cin >> a[i][j];
	cin >> n;
	for(int i=1; i<=n; i++){
		cin >> x >> y;
		for(int j=1; j<=19; j++){
			if(a[x][j]==1) a[x][j]=0;
			else a[x][j]=1;
		}
		for(int i=1; i<=19; i++){
			if(a[i][y]==1) a[i][y]=0;
			else a[i][y]=1;
		}
	}
	for(int i=1; i<=19; i++){
		for(int j=1; j<=19; j++)
			cout << a[i][j] << " ";
		cout << endl;	
	}
	return 0;
}