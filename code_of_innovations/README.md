## dependency 

We use an open source tool named "svdfeature" to optimize our MF and regression models.
The complied bin files of svdfeature are in svdfeature_bin/ 

svdfeature can be downloaded from website of SJTU apex lab:  http://apex.sjtu.edu.cn/apex_wiki/svdfeature

(We also recommend libFM and gbm for this task.)

## usage:
    >>cd bin
    >>chmod u+x *.sh
    >>chmod u+x ../svdfeature_bin/*
    >>./run_prepare.sh
    >>./run_predict_all.sh

## output

File for submission is result/output_all_post.csv 

## experiments on validation set
    >>cd bin
    >>./run_prepare.sh
    >>./run_predict_validation.sh

## author

Any question, please contact:  Zuotao Liu(zuotaoliu@126.com)
  
