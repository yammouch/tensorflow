import csv

rd = csv.reader(open('td000.csv', 'r'))

l = []
for row in rd:
  l[len(l):] = [map(float, row)]

print l[0:4]
print len(l)
