x = str(input()).lower()
set_x = list(set(x))

cnt = []
for i in set_x:
    count = x.count(i)
    cnt.append(count)
if cnt.count(max(cnt)) >= 2:
    print("?")
else:
    print(set_x[cnt.index(max(cnt))].upper())
