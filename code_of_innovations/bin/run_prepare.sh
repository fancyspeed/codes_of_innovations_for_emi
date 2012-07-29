#! /bin/bash

#split validataion set
echo "split validation..."
cd ../src/preprocess
python split_validation.py ../../data/raw_data/train.csv ../../data/validation/my_train.csv ../../data/validation/my_test.csv
cd ../../bin

#transform words.csv
echo "transform words.csv..."
cd ../src/preprocess
python process_words.py ../../data/mid_data/words_process.csv ../../data/mid_data/words.mid.csv ../../data/mid_data/words.new.csv ../../data/mid_data/mapping_2th_column.txt ../../data/mid_data/mapping_3th_column.txt

echo "trainsform users.csv..."
python make_users_file_with_meta.py ../../data/raw_data/users.csv ../../data/mid_data/users_file_meta/ ../../data/mid_data/users.new.csv
cd ../../bin


