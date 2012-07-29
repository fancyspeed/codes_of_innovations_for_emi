#! /bin/bash

#group data
echo "grouping data..."
cd ../src/preprocess
sh rebulid_train.sh ../../data/raw_data/train.csv ../../data/mid_data/rec_log_train.group
sh rebulid_test.sh ../../data/mid_data/test_5_columns.csv ../../data/mid_data/rec_log_test.group
rm *.dat
rm *.order
cd ../../bin

#train and test
echo "model 1, training and testing..."
cd ../src/model_1
sh start.sh ../../svdfeature_bin ../../data/mid_data/rec_log_train.group ../../data/mid_data/rec_log_test.group ../../data/mid_data/words.new.csv ../../data/mid_data/users.new.csv ../../data/mid_data/test_5_columns.csv
cd ../../bin
echo "model 2, training and testing..."
cd ../src/model_2
sh start.sh ../../svdfeature_bin ../../data/mid_data/rec_log_train.group ../../data/mid_data/rec_log_test.group ../../data/mid_data/words.new.csv ../../data/mid_data/users.new.csv ../../data/mid_data/test_5_columns.csv 
cd ../../bin

#post-process
echo "get stat info"
cd ../src/ensemble
python calculate_art_uid_ave.py ../../data/raw_data/train.csv ../../data/mid_data/art_uid_ave.dat
python calculate_uid_ave.py ../../data/raw_data/train.csv ../../data/mid_data/uid_ave.dat 
python calculate_user_rating_stat.py ../../data/raw_data/train.csv ../../data/mid_data/user_stat_ratings.lst 

echo "ensemble"
python simple_ensemble.py ../model_1/result/output.csv ../model_2/result/output.csv ../../result/output_all.csv
echo 'post process'
python postprocess.py ../../result/output_all.csv ../../result/output_all_post.csv ../../data/mid_data/art_uid_ave.dat ../../data/mid_data/uid_ave.dat ../../data/mid_data/user_stat_ratings.lst
cd ../../bin 

