#include <iostream>
using namespace std;

int main(){
	int a[11][11]={};
	int i, j;
	for(i=1; i<=10; i++)
		for(j=1; j<=10; j++)
			cin >> a[i][j];
	i=j=2;
	while(a[i][j]!=2){
		a[i][j]=9;
		if(a[i][j+1]!=1) ++j;
		else if(a[i+1][j]!=1) ++i;
		else break;
	}
	a[i][j]=9;
	for(i=1; i<=10; i++){
		for(j=1; j<=10; j++)
			cout << a[i][j] << " ";
		cout << endl;
	}
	return 0;
}