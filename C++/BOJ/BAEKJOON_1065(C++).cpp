#include <iostream>
using namespace std;

void Han(int n){
	if(n<100)
		cout << n << endl;
	else{
		int cnt=99, a, b, c;
		for(int i=100; i<=n; i++){
			a=i/100;
			b=i/10%10;
			c=i%10;
			if((c-b)==(b-a))
				cnt++;
		}
		cout << cnt << endl;
	}
}

int main(){
	int n;
	cin >> n;
	Han(n);
	return 0;
}