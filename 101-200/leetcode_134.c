int canCompleteCircuit(int* gas, int gasSize, int* cost, int costSize) {
    int i = 0;
    int all_gas = 0;
    int all_cost = 0;
    for(i = 0;i < gasSize;i++)
    {
        all_cost += cost[i];
        all_gas += gas[i];
    }
    if(all_cost > all_gas)
        return -1;
    for(i = 0;i < gasSize;i++)
    {
        if(gas[i] > cost[i])
        {
            all_cost = 0;
            all_gas = 0;
            for(int j = i;;j++)
            {
                if(j == gasSize)
                    j = 0;
                all_cost += cost[j];
                all_gas += gas[j];
                if(all_cost > all_gas)
                    break;
                if(j + 1 == i||(i == 0&&j == gasSize - 1))
                    return i;
           }
        }
    }

    return 0;
}
