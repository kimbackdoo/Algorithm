#include <iostream>
using namespace std;

int main(){
	int arr[3], t=0;
	for(int i=0; i<3; i++)
		cin >> arr[i];
	for(int i=0; i<3; i++)
		for(int j=0; j<2; j++)
			if(arr[j] >= arr[j+1]){
				t = arr[j];
				arr[j] = arr[j+1];
				arr[j+1] = t;
			}
	cout << arr[1] << endl;
	return 0;
}