x = str(input())
arr_list = ['c=','c-','dz=','d-','lj','nj','s=','z=']

for i in arr_list:
    x = x.replace(i, 'X')
print(len(x))
