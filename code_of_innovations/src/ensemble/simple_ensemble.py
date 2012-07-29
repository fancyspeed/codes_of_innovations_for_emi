#!/usr/bin/python

def ensemble(p_in1, p_in2, p_out):
  f_in1 = open(p_in1)
  f_in2 = open(p_in2)
  f_out = open(p_out, 'w')

  f_out.write(f_in1.readline().strip() + '\n')
  f_in2.readline()

  for line in f_in1:
    artist, track, user, score, month = line.strip().split(',')
    artist, track, user, score2, month = f_in2.readline().strip().split(',')

    new_score = float(score) * 0.5 + float(score2) * 0.5
    new_line = '%s,%s,%s,%f,%s\n' % (artist, track, user, new_score, month)

    f_out.write(new_line)

  f_out.close()
  f_in1.close()
  f_in2.close()


if __name__ == '__main__':
  import sys
  if len(sys.argv) < 4:
    print '<usage>input1 input2 output'
    exit(-1)
  p_in1 = sys.argv[1]
  p_in2 = sys.argv[2]
  p_out = sys.argv[3]

  ensemble(p_in1, p_in2, p_out)
