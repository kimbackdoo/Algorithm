#include <iostream>
using namespace std;

int main(){
	int arr[5];
	int m1, m2;
	for(int i=0; i<5; i++)
		cin >> arr[i];
	m1=arr[0], m2=arr[3];
	for(int i=0; i<3; i++)
		if(m1>arr[i])
			m1=arr[i];
	if(m2>arr[4])
		m2=arr[4];
	cout << m1+m2-50 << endl;
	return 0;
}