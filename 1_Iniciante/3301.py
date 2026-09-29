h, z, l = map(int,input().split())

# if (h < z and h > l) or (h < l and h > z):
#     print("huguinho")

# if (l < z and l > h) or (l < h and l > z):
#     print("luisinho")

# if (z < l and z > h) or (z < h and z > l):
#     print("zezinho")

nomes = {h: "huguinho", z: "zezinho", l: "luisinho"}
print(nomes[sorted([h,z,l])[1]])