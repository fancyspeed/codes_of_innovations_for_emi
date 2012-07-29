#!/usr/bin/python
#coding=utf8
import gc

gc.disable()

p_pred = 'pred.txt'

def pred(p_group, p_test, p_out):
  f_pred = open(p_pred)
  f_out = open(p_out,'w')
  f_group = open(p_group)
  f_test = open(p_test)

  f_out.write(f_test.readline())

  pred_hash = {}

  for line in f_group:
      user, artist, track, month, score = line.strip().split('\t')
      #user, track, score, artist, month = line.strip().split('\t')

      pred = float(f_pred.readline().strip())

      if pred < 0:
          pred = float(0)
      if pred > 100:
          pred = float(100)

      key = int(track) * 100000 + int(user)
      if key in pred_hash:
          print 'key already exists:', track, user
          exit(-1)
      else:
          pred_hash[key] = pred

  for line in f_test:
      artist, track, user, score, month = line.strip().split(',')

      key = int(track) * 100000 + int(user)
      if key in pred_hash:
          f_out.write('%s,%s,%s,%f,%s\n' % (artist, track, user, pred_hash[key], month))
      else:
          print 'can not find key:', track, user
          exit(-1)

  f_test.close()
  f_pred.close()
  f_out.close()
  f_group.close()

if __name__=="__main__":
    import sys
    if len(sys.argv) < 4:
        print '<usage> group test output'
        exit(-1)
    p_group = sys.argv[1]
    p_test = sys.argv[2]
    p_out = sys.argv[3]

    pred(p_group, p_test, p_out)

