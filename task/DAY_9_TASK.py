def integer_square_root(k):
    if k==0 or k==1:
        return k
    low=1
    high=k
    while(low<=high):
        mid=(low+high)//2

        if mid*mid==k:
            return mid
        if mid**2 <k:
            low=mid+1
            ans=mid
        else:
            high=mid-1
    return ans        
print(integer_square_root(101))