#!/bin/bash
python create_group_test.py $1 ./rec_log_test_group.dat 
../../svdfeature_bin/svdpp_randorder ./rec_log_test_group.dat ./rec_log_test.order
../../svdfeature_bin/line_reorder ./rec_log_test_group.dat ./rec_log_test.order $2 
