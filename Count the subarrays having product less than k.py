n = int(input())
k = int(input())
a = list(map(int,input().split()))
left, count = 0,0
product =1
for right in range(n):
    product*= a[right]
    while(product>=k):
        product/=a[left]
        left+=1
    count+= right+left-1
print(count)
