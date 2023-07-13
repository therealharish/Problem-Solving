#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>

using namespace std;
using namespace __gnu_pbds;

typedef long long ll;
typedef tree<int, null_type, less<int>, rb_tree_tag, tree_order_statistics_node_update> ordered_set;

int main()
{
    ll n, p;
    cin >> n >> p;

    vector<ll> vec(n);
    ordered_set stt;
    map<ll, ll> mp;

    for (int i = 0; i < n; i++) {
        cin >> vec[i];
        if (mp[vec[i]] == 0) {
            stt.insert(vec[i]);
            mp[vec[i]] = 1;
        }
    }

    for (int i = 0; i < p; i++) {
        ll x;
        cin >> x;

        if (mp[x] == 0) {
            stt.insert(x);
            mp[x] = 1;
        }
        cout << stt.size() - stt.order_of_key(x) << endl;
    }
}