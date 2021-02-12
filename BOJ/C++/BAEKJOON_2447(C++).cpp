#include <iostream>
#include <cstring>
using namespace std;

char s[2201][2201];

void Star(int x, int y, int n){
	if(n==1){
		s[x][y]='*';
		return;
	}
	int d=n/3;
	for(int i=0; i<3; i++)
		for(int j=0; j<3; j++){
			if(i==1&&j==1) continue;
			else Star(x+(i*d),y+(j*d),d);
		}
}

int main(){
	int n;
	cin >> n;
	memset(s,' ',sizeof(s));
	Star(0,0,n);
	for(int i=0; i<n; i++){
		for(int j=0; j<n; j++)
			cout << s[i][j];
		cout << endl;
	}
	return 0;
}