N = 5
words = ["act","god","cat","dog","tac"]
d= {}
for i in words:
    j = "".join(sorted(i))
    if j not in d:
        d[j] = [i]
    else:
        d[j].append(i)
print(d)
ans = []
for i in d:
    ans.append(d[i])
print(*ans)

