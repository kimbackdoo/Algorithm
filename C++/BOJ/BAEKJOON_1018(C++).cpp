#include <iostream>
#include <cmath>
using namespace std;

int main(){
	char chess[51][51];
	int n, m, mn=80, cntW, cntB;
	cin >> n >> m;
	for(int i=0; i<n; i++)
		scanf("%s", &chess[i]);
	for(int i=0; i<n-7; i++){
		for(int j=0; j<m-7; j++){
			cntW=0, cntB=0;
			for(int a=i; a<i+8; a++){
				for(int b=j; b<j+8; b++){
					if((a+b)%2==0){
						if(chess[a][b]=='B') cntW++;
						else cntB++;
					}
					else{
						if(chess[a][b]=='B') cntB++;
						else cntW++;
					}
				}
			}
			mn=min(mn, cntB);
			mn=min(mn, cntW);
		}
	}
	cout << mn << endl;
	return 0;
}