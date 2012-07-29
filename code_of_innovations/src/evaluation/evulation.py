#!/usr/bin/python

def evaluate_RMSE(p_pred, p_truth, all_flag=False):
  '''
  parameter p_pred: file of prediction
  parameter p_truth: file of groundtruth(train.csv)
  parameter all_flag: if prediction is in 1-column, all_flag=False; if in 5-column, all_flag=True 
  '''

  f_pred = open(p_pred)
  f_truth = open(p_truth)

  n_line = 0
  n_tot = 0

  f_truth.readline()
  f_pred.readline()

  for line in f_truth:
    artist, track, user, rate, time = line.strip().split(',')
    if all_flag:
      art2, track2, user2, pred, time2 = f_pred.readline().strip().split(',')
    else:
      pred = f_pred.readline().strip()

    err = float(pred) - float(rate)

    n_line += 1
    n_tot += err*err

  import math
  rmse = math.sqrt(n_tot / n_line)
  return rmse, n_line, n_tot


if __name__ == '__main__':
  import sys
  if len(sys.argv) <= 2:
    print '<usage>groundtruth prediction [all(if in 5-column)]'
    exit(-1)

  p_truth = sys.argv[1]
  p_pred = sys.argv[2]
  all_flag = False
  if len(sys.argv) >= 4:
    all_flag = True

  rmse, n_line, n_tot = evaluate_RMSE(p_pred, p_truth, all_flag)
  print 'rmse =', rmse

