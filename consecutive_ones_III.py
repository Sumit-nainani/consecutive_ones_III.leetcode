# Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array 
# if you can flip at most m 0's.

# approach:
    #   traverse the array if there is 1 then increment your answer by 1 ,
    #   if there is 0 and you can flip 0 to 1 then decrement m by 1 and update answer 
    #   if you dont have anymore m then traverse the array with start pointer until you get encounter with a 0.
def traffic(n: int, m: int, vehicle: [int]) -> int:
    # Write your code here.
    e=0
    s=0
    ans=0
    while e<n:
        if vehicle[e]==0:
            if m:
                m-=1
            else:
                while m==0:
                    if vehicle[s]==0:
                        m+=1
                    s+=1
                m-=1
                
        ans=max(ans,e-s+1)
        e+=1
    return ans
