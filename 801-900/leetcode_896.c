bool isMonotonic(int* A, int ASize) {
    int i;
    int l = 0;
    for(i = 0;i < ASize - 1;i++)
        if(A[i] != A[i + 1])
            break;
    if(A[i] > A[i + 1])
        l = 1;
    else 
        l = 2;
    for(;i < ASize - 1;i++)
        if(l == 1&&A[i] < A[i + 1])
            break;
        else if(l == 2&&A[i] > A[i + 1])
            break;
    if(i == ASize - 1)
        return true;
    else
        return false;
}