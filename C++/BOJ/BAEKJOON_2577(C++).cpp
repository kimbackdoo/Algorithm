#include <iostream>
using namespace std;

int main(){
	int a, b, c, t, arr[10]={};
	cin >> a >> b >> c;
	t = a*b*c;
	while(t>0){
		arr[t%10]++;
		t/=10;
	}
	for(int i=0; i<10; i++)
		cout << arr[i] << endl;
	return 0;
}