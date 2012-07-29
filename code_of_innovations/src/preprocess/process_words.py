#!/usr/bin/python

def trans_input_2_mid(p_input, p_mid, p_map_2, p_map_3):
  f_words = open(p_input)
  f_mid = open(p_mid, 'w')

  headline = f_words.readline()
  arr_head = headline.strip().split(',')

  map_2 = {}
  map_3 = {}

  for line in open(p_map_2):
    key, value = line.strip().split(',')
    map_2[key] = value

  for line in open(p_map_3):
    key, value = line.strip().split(',')
    map_3[key] = value
  
  for line in f_words:
    arr = line.strip().split(',') 
    len_arr = len(arr)

    new_line = []
    new_line.append(arr[0]) #artist
    new_line.append(arr[1]) #user
    if arr[4] == '': #like_artist
      new_line.append('-1')
    else:
      new_line.append(arr[4])
  
    if arr[2] != '':
      new_line.append( map_2[arr[2]] )
    if arr[3] != '':
      new_line.append( map_3[arr[3]] )

    for i in range(5, len_arr):
      if arr[i] == '1':
        new_line.append(arr_head[i])

    new_line_str = '\t'.join(new_line)
    f_mid.write(new_line_str + '\n')

  f_mid.close()
  f_words.close()


def trans_mid_2_output(p_mid, p_out):
  f_out = open(p_out, 'w')

  word_map = {}
  cur_value = 0

  for line in open(p_mid):
    arr = line.strip().split('\t') 

    f_out.write('%s\t%s\t%s' % ( arr[0], arr[1], int(float(arr[2])) ))

    for i in range(3, len(arr)):
      if arr[i] not in word_map:
        cur_value += 1
        word_map[arr[i]] = cur_value

      f_out.write('\t%d' % word_map[arr[i]])
    f_out.write('\n')
     
  f_out.close()


if __name__ == '__main__':
  import sys
  if len(sys.argv) < 6:
    print '<usage>input mid output map_2 map_3' 
    exit(-1)

  p_input = sys.argv[1] 
  p_mid = sys.argv[2]
  p_out = sys.argv[3]
  p_map_2 = sys.argv[4]
  p_map_3 = sys.argv[5]

  trans_input_2_mid(p_input, p_mid, p_map_2, p_map_3)
  trans_mid_2_output(p_mid, p_out)

