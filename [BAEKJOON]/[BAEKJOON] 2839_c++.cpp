#include <iostream>
using namespace std;
int main() {
	int n;
	int bag = 0;

	cin >> n;

	while (1) {
		if (n % 5 == 0) {
			bag = bag + n / 5;
			cout << bag << endl;
			break;
		}
		else {
			n = n - 3;
			if (n < 0) {
				cout << "-1" << endl;
				break;
			}
			bag++;
		}
	}
	return 0;
}