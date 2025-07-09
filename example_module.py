def find_missing_number(A:list, p:int, q:int) -> int:
    '''
    This code will find the missing number in a list in the ascending order.
    '''
    # base case
    if p>=q:
        #print(A[p]-1)
        return (A[p]-1)
    m = (p+q)//2
    #print(p,q,m,A[m],A[p])
    if (m-p!=A[m]-A[p]):
        return find_missing_number(A,p,m)
    else:
        return find_missing_number(A,m+1,q)

def counting_sort(A:list, n:int):
    '''
    A is the array to be sorted
    n is the maximum value of an element in the array
    A is not affected by the sort
    '''
    m = len(A)
    C = [None]*(n+1)
    B=[None]*len(A)

    # print(C)
    for i in range(0,n+1):
        C[i] = 0
    for i in range(0,m):
        # print(A[i])
        C[A[i]] = C[A[i]]+1
    # print(C)
    for i in range(1,n+1):
        C[i] = C[i] + C[i-1]
    # print(C)
    for i in range(0,m):
        B[C[A[i]]-1] = A[i] # A[i]-1 to compensate for 0-index in Python
        C[A[i]] = C[A[i]] - 1
    return B


if __name__=="__main__":
    print(counting_sort([4,2,3,3,2],4))