#include <iostream>
using namespace std;

int main(){
	int n, cnt=0;
	string s;
	cin >> n;
	for(int i=0; i<n; i++){
		cin >> s;
		bool check=true;
		for(int j=0; s[j]; j++)
			for(int k=0; k<j; k++)
				if(s[j]!=s[j-1]&&s[j]==s[k]){
					check=false;
					break;
				}
		if(check) cnt++;		
	}
	cout << cnt << endl;
	return 0;
}