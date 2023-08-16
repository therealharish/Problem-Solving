long findTotalExecutionTime(vector<int> execution)
{
    int n = execution.size();
    map<int, long> mpp;
    long placementlelo = 0;
    for (auto a : execution)
    {
        if (!mpp.count(a))
        {
            mpp[a] = (a + 1) / 2;
            placementlelo = placementlelo + a
        }
        else
        {
            placementlelo = placementlelo + mpp[a];
            mpp[a] = (mpp[a] + 1) / 2;
        }
    }
    return placementlelo;
}