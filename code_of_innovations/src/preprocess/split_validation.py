#!/usr/bin/python

def split_for_validataion(p_rawdata, p_train, p_valid):
  f_raw = open(p_raw)
  f_train = open(p_train, 'w')
  f_valid = open(p_valid, 'w')

  line_head = f_raw.readline()
  f_train.write(line_head)
  f_valid.write(line_head)

  import random

  for line in f_raw:
    if 1== random.randint(0,4):
      f_valid.write(line)
    else:
      f_train.write(line)


  f_valid.close()
  f_train.close()
  f_raw.close()


if __name__ == '__main__':
  import sys
  if len(sys.argv) < 4:
    print '<usage>raw_train new_train new_validation'
    exit(-1)

  p_raw = sys.argv[1] 
  p_train = sys.argv[2]
  p_valid = sys.argv[3]

  split_for_validataion(p_raw, p_train, p_valid)

