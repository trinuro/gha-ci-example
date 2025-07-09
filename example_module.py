def sum(input: list) -> int:
    output = 0
    for i in input:
        output += i 
    return output

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
