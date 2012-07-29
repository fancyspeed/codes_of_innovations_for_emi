#!/bin/bash
python create_group_train.py $1 ./rec_log_train_group.dat 
../../svdfeature_bin/svdpp_randorder ./rec_log_train_group.dat ./rec_log_train.order
../../svdfeature_bin/line_reorder ./rec_log_train_group.dat ./rec_log_train.order $2 
