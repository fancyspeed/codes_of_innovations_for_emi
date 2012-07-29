#!/bin/bash

function check_ret {
    ret=$1
    if ((ret+0 != 0)); then
        echo -e "ERROR["$ret"]:"
        exit $ret
    fi
}

if (($# != 6)); then
    echo $#
    echo '<usage> svdfeature_path train_group test_group words users test'
    p_train_group='../../data/validation/rec_log_train.group'
    p_test_group='../../data/validation/rec_log_test.group'
    p_test='../../data/validation/my_test.csv'
    p_svdfeature='../../svdfeature_bin'
    p_words='../../data/mid_data/words.new.csv'
    p_users='../../data/mid_data/users.new02.csv'
else
    p_svdfeature=$1
    p_train_group=$2
    p_test_group=$3
    p_words=$4
    p_users=$5
    p_test=$6
fi

echo "svdfeature", ${p_svdfeature}
echo "train_group", ${p_train_group}
echo "test_group", ${p_test_group}
echo "words", ${p_words}
echo "users", ${p_users}
echo "test", ${p_test}

rm -f result/pred.txt
rm -f result/output.csv

echo "start"
echo `date`

python make_features.py ${p_train_group} tmp_data/rec_log_train.basicfeature ${p_words} ${p_users}
check_ret $?
python make_features.py ${p_test_group} tmp_data/rec_log_test.basicfeature ${p_words} ${p_users}
check_ret $?

${p_svdfeature}/make_ugroup_buffer tmp_data/rec_log_train.basicfeature tmp_data/rec_log_train.snsbuffer
check_ret $?
${p_svdfeature}/make_ugroup_buffer tmp_data/rec_log_test.basicfeature tmp_data/rec_log_test.snsbuffer 
check_ret $?

${p_svdfeature}/svd_feature svdfeature.conf  buffer_feature="tmp_data/rec_log_train.snsbuffer" model_out_folder="model_data"  num_round=1
check_ret $?
${p_svdfeature}/svd_feature_infer svdfeature.conf model_out_folder="model_data" pred=1
check_ret $?

python ./calc.py ${p_test_group} ${p_test}
check_ret $?

mv ./pred.txt result/pred.txt 
mv ./output.csv result/output.csv

echo 'end success'
echo `date`

