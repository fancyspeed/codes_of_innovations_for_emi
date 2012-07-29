import gc
gc.disable();

import sys
file = open(sys.argv[1])
file.readline()
out = open(sys.argv[2], 'w')

data = {}

for line in file:
    art, track, user, rate, month = line.strip(' \n\r').split(',')
    data.setdefault(user,[])
    data[user].append( (art, track, month, '0') )

for i in data:
    for each in data[i]:
        out.write('%s\t%s\t%s\t%s\t%s\n'%(i,each[0],each[1],each[2],each[3]))

file.close()
out.close()

