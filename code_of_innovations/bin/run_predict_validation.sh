#! /bin/bash

#group data
echo "grouping data..."
cd ../src/preprocess
sh rebulid_train.sh ../../data/validation/my_train.csv ../../data/validation/rec_log_train.group
sh rebulid_test.sh ../../data/validation/my_test.csv ../../data/validation/rec_log_test.group
rm *.dat
rm *.order
cd ../../bin

# model 1: train and test
echo "model 1, training and testing..."
cd ../src/model_1
sh start.sh ../../svdfeature_bin ../../data/validation/rec_log_train.group ../../data/validation/rec_log_test.group ../../data/mid_data/words.new.csv ../../data/mid_data/users.new.csv ../../data/validation/my_test.csv
cd ../../bin
echo "model 2, training and testing..."
cd ../src/model_2
sh start.sh ../../svdfeature_bin ../../data/validation/rec_log_train.group ../../data/validation/rec_log_test.group ../../data/mid_data/words.new.csv ../../data/mid_data/users.new.csv ../../data/validation/my_test.csv
cd ../../bin

# get RMSE 
cd ../src/evaluation
echo 'model 1, evaluating'
python metric_RMSE.py ../../data/validation/my_test.csv ../model_1/result/output.csv all
echo 'model 2, evaluating'
python metric_RMSE.py ../../data/validation/my_test.csv ../model_2/result/output.csv all
cd ../../bin

#post-process
cd ../src/ensemble
echo "get stat info"
python calculate_art_uid_ave.py ../../data/validation/my_train.csv ../../data/mid_data/art_uid_ave_mytrain.dat
python calculate_uid_ave.py ../../data/validation/my_train.csv ../../data/mid_data/uid_ave_mytrain.dat 
python calculate_user_rating_stat.py ../../data/validation/my_train.csv ../../data/mid_data/user_stat_ratings_mytrain.lst 

echo "ensemble"
python simple_ensemble.py ../model_1/result/output.csv ../model_2/result/output.csv ../../result/output_validation.csv
echo 'post process'
python postprocess.py ../../result/output_validation.csv ../../result/output_validation_post.csv ../../data/mid_data/art_uid_ave_mytrain.dat ../../data/mid_data/uid_ave_mytrain.dat ../../data/mid_data/user_stat_ratings_mytrain.lst
cd ../../bin 

cd ../src/evaluation
echo 'evaluating after ensemble'
python metric_RMSE.py ../../data/validation/my_test.csv ../../result/output_validation.csv all
echo 'evaluating after postprocess'
python metric_RMSE.py ../../data/validation/my_test.csv ../../result/output_validation_post.csv all
cd ../../bin

