import csv

rd = csv.reader(open('td000.csv', 'r'))

def move_left(schem):
  col0 = map(lambda row: row[0], schem)
  col0_is_empty = map(lambda x: x == '00', col0)
  if all(col0_is_empty):     
    return map(lambda row: row[1:] + ['00'], schem)
  else:
    return None

def move_right(schem):
  col_last = map(lambda row: row[-1], schem)
  col_last_is_empty = map(lambda x: x == '00', col_last)
  if all(col_last_is_empty):
    return map(lambda row: ['00'] + row[0:-1], schem)
  else:
    return None

def move_up(schem):
  if all(map(lambda x: x == '00', schem[0])):
    return schem[1:] + ['00' * 20]
  else:
    return None

def move_down(schem):
  if all(map(lambda x: x == '00', schem[-1])):
    return ['00' * 20] + schem[0:-1]
  else:
    return None

schem = []
for row in rd:
  schem = schem + [row]

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
