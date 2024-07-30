#include <iostream>
#include <cstring>
using namespace std;

int main(){
	int n, cnt, result;
	char ch[100][81];
	cin >> n;
	for(int i=0; i<n; i++)
		cin >> ch[i];
	for(int i=0; i<n; i++){
		cnt=result=0;
		for(int j=0; j<strlen(ch[i]); j++){
			if(ch[i][j]=='O'){
				cnt++;
				result+=cnt;
			}
			else cnt=0;
		}
		cout << result << endl;
	}
	return 0;
}