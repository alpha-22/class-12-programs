#include<bits/stdc++.h>
using namespace std;
#define pb push_back
void func(std::vector<int> a, int ts)
{
	int i = 0;
	int j = a.size() - 1;
	//cout << ts << endl;
	sort(a.begin(), a.end());
	while (i < j)
	{
		int sum = a[i] + a[j];
		if (sum < ts)
			i++;
		else if (sum > ts)
			j--;
		else if (sum == ts)
		{
			cout << a[i] << " and " << a[j] << endl;
			i++;
			j--;
		}
	}

}
int main()
{
#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	int n;
	cin >> n;
	int a;
	std::vector<int> v;
	for (int i = 0; i < n; i++)
	{
		cin >> a;
		v.pb(a);
	}
	int ts;
	cin >> ts;
	func(v, ts);

}