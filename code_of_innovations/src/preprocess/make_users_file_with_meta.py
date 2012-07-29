import sys
import os
import hashlib
import time

reload(sys)
sys.setdefaultencoding('utf-8')

gender_dict = {}
working_status_dict = {}
region_dict = {}
music_dict = {}
list_back_dict = {}
list_own_dict = {}

total_dict = {}

def load_meta(p_meta_dir):
    dirname = p_meta_dir
    
    for line in open(dirname + "map_gender.map"):
        rt = line.strip().split('\t')
        gender_dict[rt[0]] = rt[1]
        total_dict[rt[0]] = rt[1]
    
    for line in open(dirname + "map_list_back.map"):
        rt = line.strip().split('\t')
        list_back_dict[rt[0]] = rt[1]
        total_dict[rt[0]] = rt[1]
            
    for line in open(dirname + "map_list_own.map"):
        rt = line.strip().split('\t')
        list_own_dict[rt[0]] = rt[1]
        total_dict[rt[0]] = rt[1]
            
    for line in open(dirname + "map_music_value.map"):
        rt = line.strip().split('\t')
        music_dict[rt[0]] = rt[1]
        total_dict[rt[0]] = rt[1]
                    
    for line in open(dirname + "map_region_value.map"):
        rt = line.strip().split('\t')
        region_dict[rt[0]] = rt[1]
        total_dict[rt[0]] = rt[1]
            
    for line in open(dirname + "map_working_status.map"):
        rt = line.strip().split('\t')
        working_status_dict[rt[0]] = rt[1]
        total_dict[rt[0]] = rt[1]
            
    print 'load meta data done!'

def make_users_csv_with_meta(path, outpath):
    fout = open(outpath, 'w')
    line_count = 0
    for line in open(path):
        line_count += 1
        if line_count == 1:
            continue

        rt = line.strip().split(',')
        for i in range(len(rt)):
            if i != 0:
                fout.write(",")
            value = rt[i]
            if value == "":
                value = -1
            elif total_dict.has_key(rt[i]):
                value = total_dict[rt[i]]                
            fout.write("%s" %(value))
        fout.write("\n")
    
if __name__ == '__main__':
    import sys
    if len(sys.argv) < 4:
        print '<usage> python make_users_file_with_meta raw_users.csv, meta_dir, output_file'
        print 'example: python make_users_file_with_meta.py ../../data/raw_data/users.csv ../../data/mid_data/users_file_meta/ ./users.new.csv'
        exit(-1)
        
    p_input = sys.argv[1]
    p_meta_dir = sys.argv[2]
    p_output = sys.argv[3]
    
    load_meta(p_meta_dir)
    #make_users_csv_with_meta("../raw_data/users.csv", "./users01.csv")
    make_users_csv_with_meta(p_input, p_output)
