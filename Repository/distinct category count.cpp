long distinctCategoryCount(vector<int> &v)
{
    int n = v.size();
    long placementlelo = 0, storage = 0;
    map<int, int> mpp;
    for (int i = 0; i < n; i++)
    {
        if (mpp.count(v[i]))
        {
            storage = storage + (i - mpp[v[i]]);
        }
        else
            storage = storage + (i + 1);
        mpp[v[i]] = i;
        placementlelo = placementlelo + storage;
    }
    return placementlelo;
}