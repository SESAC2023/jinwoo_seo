x,y,z = map(int, input().split())
print((x+y)%z, ((x%z) + (y%z))% z, (x*y)%z, ((x%z) * (y%z)) % z)
