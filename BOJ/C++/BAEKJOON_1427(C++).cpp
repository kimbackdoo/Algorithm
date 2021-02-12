#include <iostream>
using namespace std;

int main(){
	int cnt=0, t[11];
	char n[11];
	scanf("%s", n);
	for(int i=0; n[i]; i++){
		t[i]=n[i]-'0';
		cnt++;
	}
	for(int i=0; i<cnt; i++)
		for(int j=i+1; j<cnt; j++)
			if(t[i]>t[j]){
				int tmp=t[i];
				t[i]=t[j];
				t[j]=tmp;
			}
	for(int i=cnt-1; i>=0; i--)
		cout << t[i];
	return 0;
}