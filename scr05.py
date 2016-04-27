import csv

rd = csv.reader(open('td000.csv', 'r'))

def all0(l):
  return all(map(lambda el: el == 0, l))

def move_left(schem):
  empty_el = [0.] * 7
  col0 = map(lambda row: row[0], schem)
  col0_is_empty = map(all0, col0)
  if all(col0_is_empty):     
    return map(lambda row: row[1:] + [empty_el], schem)
  else:
    return None

def move_right(schem):
  empty_el = [0.] * 7
  col_last = map(lambda row: row[-1], schem)
  col_last_is_empty = map(all0, col_last)
  if all(col_last_is_empty):
    return map(lambda row: [empty_el] + row[0:-1], schem)
  else:
    return None

def move_up(schem):
  if all(map(all0, schem[0])):
    return schem[1:] + [[[[0.] * 7] * 20]]
  else:
    return None

def move_down(schem):
  if all(map(all0, schem[-1])):
    return [[[[0.] * 7] * 20]] + schem[0:-1]
  else:
    return None

l = []
for row in rd:
  l[len(l):] = [map(float, row)]

schem = []
while l:
  schem, l = schem + [l[0:20]], l[20:]

schem_hor = [schem]
schem_tmp = move_left(schem)
while schem_tmp:
  schem_hor = [schem_tmp] + schem_hor
  schem_tmp = move_left(schem_tmp)
schem_tmp = move_right(schem)
while schem_tmp:
  schem_hor = schem_hor + [schem_tmp]
  schem_tmp = move_right(schem_tmp)
  
print len(schem_hor)
