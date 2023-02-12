a = list(map(str, input()))
h = []
zero = []
one = []
l = 0
p = 0
o = 0
g = 0
h = list(map(ord, a))
h = list(map(bin, h)) 
for k in range(len(h)):
  g = str(h[k])
  l = list(map(str, g))
  l.remove("b")
  l = list(map(int, l))
  for i in range(len(l)):
    if i == 0:
      if l[i + 1] + l[len(l) - 1] != 1 and l[i] == 1:
        zero.append(i)
      elif l[i + 1] + l[len(l) - 1] > 0 and l[i] == 0:
        one.append(i)
    elif i == len(l) - 1:
      if l[i - 1] + l[0] != 1 and l[i] == 1:
        zero.append(i)
      elif l[i - 1] + l[0] > 0 and l[i] == 0:
        one.append(i)
    else:
      if l[i - 1] + l[i + 1] != 1 and l[i] == 1:
        zero.append(i)
      elif l[i - 1] + l[i + 1] > 0 and l[i] == 0:
        one.append(i)
  if len(one) != 0:
    for j in range(len(one)):
      o = one[j]
      l[o] = 1
    one = []
  if len(zero) != 0:
    for z in range(len(zero)):
      p = zero[z]
      l[p] = 0
    zero = []
  l = list(map(str, l))
  h[k] = "".join(l)
for s in range(len(h)):
  h[s] = int(h[s], 2)
h = list(map(chr, h))
print(''.join(map(str, h)))
