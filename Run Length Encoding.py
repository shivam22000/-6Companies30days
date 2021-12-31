arr = "aaaabbbcccdd"
count = 1
stri = ""
i=0
while(i<len(arr)-1):
    if arr[i]==arr[i+1]:
        count+=1
        i+=1
    else:
        stri+=(arr[i]+str(count))
        i+=1
        count=1
stri+=arr[i]+str(count)
print(stri)