n = int(input())
dp = [0]*(n)
dp[0] = 1
i,j,k=1,1,1
for l in range(1,n):
    dp[l] = min(2*i,3*j,5*k)
    if dp[l] == i*2:
        i+=1
    if dp[l] == j*3:
        j+=1
    if dp[l] == k*5:
        k+=1
print(dp[-1])