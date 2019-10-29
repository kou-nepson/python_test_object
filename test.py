import re

text = ""
with open("input.txt", "r") as f:
    text = f.read()

s = []
i = []
m = []
dct = {}

s = text.splitlines()

print(s)

print(len(s))
for j in range(len(s)-1):
    d = s[j].split(":")
    dct[int(d[0])] = d[1]
M = s[len(s)-1]

dct = sorted(dct.items())

result = ""

print(dct)
for dct_key in dct:
    if int(M) % dct_key[0] == 0:
        result += dct_key[1]

print(result)
