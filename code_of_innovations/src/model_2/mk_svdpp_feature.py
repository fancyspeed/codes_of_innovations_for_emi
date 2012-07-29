#!/usr/bin/env python
#coding: utf-8
#Filename: mk_svdpp_feature.py
#Author: Yingwei Xin(xinyingwei.wei@snda.com)
#Create: 2012-07-22
#Modify: 2012-07-22

import sys
import math
import time

user_age_dict = {}
user_gender_dict = {}
user_work_dict = {}
user_region_dict = {}
user_music_dict = {}
user_own_dict = {}
user_back_dict = {}
user_habit_dict = {}

words_like_dict = {}
words_dict = {}

def load_users_new(p_users):
    file = open(p_users)
    for line in file:
        data_list = line.strip().split(',')
        
        uid = data_list[0]
        gender = data_list[1]
        age = int(data_list[2])
        work = data_list[3]
        region = data_list[4]
        music = data_list[5]
        own = data_list[6]
        back = data_list[7]

        if age >= 13 and age <= 64:
            age = 13 + age/3
        
        user_gender_dict[uid] = gender
        user_age_dict[uid] = age
        user_work_dict[uid] = work
        user_region_dict[uid] = region
        user_music_dict[uid] = music
        user_own_dict[uid] = float(own)
        user_back_dict[uid] = float(back)
        
        user_habit_dict[uid] = data_list[8:]

    file.close()


def load_words_new(p_words):
    file = open(p_words)
    for line in file:
        data_list = line.strip().split('\t')
        artist = data_list[0]
        user = data_list[1]
        like = data_list[2]
        words_like_dict[artist+'_'+user] = like
        words_dict[artist+'_'+user] = data_list[3:]
    file.close()


def mkfeature(fin, fout):
    fi = open( fin , 'r' )
    fo = open( fout, 'w' )

    for line in fi:
        uid, artist, iid, time, rating = line.strip().split('\t')
        #uid, iid, rating, artist, time = line.strip().split('\t')
       
        global_num = 2
        #dynamic
        if words_dict.has_key(artist+'_'+uid):
            global_num += len(words_dict[artist+'_'+uid])

        if words_like_dict.has_key(artist+'_'+uid):
            global_num += 1
        
        if uid in user_gender_dict:
            global_num += 2
        if uid in user_age_dict:
            global_num += 1
        if uid in user_work_dict:
            global_num += 1
        if uid in user_region_dict:
            global_num += 1
        if uid in user_music_dict:
            global_num += 1
        if uid in user_own_dict:
            global_num += 1
        if uid in user_back_dict:
            global_num += 1
        
        if uid in user_habit_dict:
            global_num += len(user_habit_dict[uid])

        fo.write('%s\t%d\t%d\t%d\t' %(rating, global_num, 1, 1))
        
        #global bias
         
        #dynamic string
        dynamic_str = ''
        if words_dict.has_key(artist+'_'+uid):
            value = pow(len(words_dict[artist+'_'+uid]), -0.5)
            for key in words_dict[artist+'_'+uid]:
                dynamic_str += key + ':' + str(value) + ' '
            fo.write('%s' %(dynamic_str))
        #like
        if words_like_dict.has_key(artist+'_'+uid):
            like = words_like_dict[artist+'_'+uid]
            fo.write('%s:1 ' %(500+int(like)))
        
        #time, artist
        fo.write('%d:1 %d:1 ' %(700+int(time), 800+int(artist)))
        
        #gender
        if uid in user_gender_dict:
            gender = user_gender_dict[uid]
            fo.write('%d:1 ' %(900+int(iid)*3+int(gender)))
        
        #age
        if uid in user_age_dict:
            age = user_age_dict[uid]
            fo.write('%d:1 ' %(2000+int(iid)*94+int(age)))
        
        #work
        if uid in user_work_dict:
            work = user_work_dict[uid]
            fo.write('%d:1 ' %(22000+int(iid)*15+int(work)))
        
        #region
        if uid in user_region_dict:
            region = user_region_dict[uid]
            fo.write('%d:1 ' %(30000+int(uid)*7+int(region)))
        
        #music
        if uid in user_music_dict:
            music = user_music_dict[uid]
            fo.write('%d:1 ' %(400000+int(uid)*7+int(music)))
        
        #own
        if uid in user_own_dict:
            own = user_own_dict[uid]
            fo.write('%d:1 ' %(800000+int(uid)*25+int(own)))
       
        #back
        if uid in user_back_dict:
            back = user_back_dict[uid]
            fo.write('%d:1 ' %(2200000+int(uid)*25+int(back)))
        
        #habit string
        habit_str = ''
        if uid in user_habit_dict:
            for i in xrange(len(user_habit_dict[uid])):
                key = 4500000 + i
                value = float(user_habit_dict[uid][i])/float(100)
                habit_str += str(key) + ':' + str(value) + ' '
            fo.write('%s' %(habit_str))
        
        #artist gender
        if uid in user_gender_dict:
            gender = user_gender_dict[uid]
            fo.write('%d:1 ' %(4510000+int(artist)*3+int(gender)))
        
        #user bias
        fo.write('%s:1 ' %(uid))

        #item bias
        fo.write('%s:1\n' %(iid))
    
    fi.close()
    fo.close()


if __name__ == '__main__':
    import sys
    if len(sys.argv) < 5:
        print '<usage> group users words output'
        exit(-1)
    p_group = sys.argv[1]
    p_users = sys.argv[2]
    p_words = sys.argv[3]
    p_output = sys.argv[4]
    
    load_users_new(p_users)
    load_words_new(p_words)
      
    mkfeature(p_group, p_output)



