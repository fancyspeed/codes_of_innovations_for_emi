#!/bin/bash

p_svdfeature=$1
p_train_group=$2
p_test_group=$3
p_words=$4
p_users=$5
p_test=$6


# generate basic feature file for user grouped training  and test data
python mk_svdpp_feature.py ${p_train_group} ${p_users} ${p_words} tmp_data/train.group.basicfeature
python mk_svdpp_feature.py ${p_test_group} ${p_users} ${p_words} tmp_data/test.group.basicfeature

#make buffer for training and test feature file
${p_svdfeature}/make_ugroup_buffer tmp_data/train.group.basicfeature tmp_data/train.group.fd_buffer 
#-fd ../data/train.group.feedbackfeature
${p_svdfeature}/make_ugroup_buffer tmp_data/test.group.basicfeature tmp_data/test.group.fd_buffer
#-fd ../data/test.group.feedbackfeature

# training for 30 rounds
${p_svdfeature}/svd_feature svd_plus_plus_fd.conf num_round=10

# write out prediction from 0030.model
${p_svdfeature}/svd_feature_infer svd_plus_plus_fd.conf pred=10

#rank final
python calc.py ${p_test_group} ${p_test} result/output.csv

