#include<iostream>
#include<cstring>
using namespace std;

int main(){
	char a[20];
	cin >> a;
	char *t = strtok(a, ".");
	while(t!=NULL){
		cout << t << endl;
		t = strtok(NULL, ".");
	}
	return 0;
}