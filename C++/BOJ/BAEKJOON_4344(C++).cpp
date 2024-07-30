#include <iostream>
using namespace std;

int main(){
	int c, n, arr[1000];
	double avg=0;
	cin >> c;
	for(int i=0; i<c; i++){
		cin >> n;
		int cnt=0, total=0;
		for(int j=0; j<n; j++){
			scanf("%d", &arr[j]);
			total+=arr[j];
		}
		for(int j=0; j<n; j++){
			avg = (total)/n;
			if(arr[j]>avg)
				cnt++;
		}
		printf("%.3lf%%\n", (double)cnt/n*100);
	}
	return 0;
}