#! /usr/bin/python
import math

user_artist_score = {}
user_artist_feat = {}
user_artists = {}

def load_words(p_words):
  for line in open(p_words):
    arr = line.strip().split('\t')
    art_i = int(arr[0])
    user_i = int(arr[1])
    
    if user_i not in user_artists:
        user_artists[user_i] = []

    key = art_i * 100000 + user_i
    
    if arr[2] != '-1':
        user_artist_score[key] = float(arr[2]) / 102.0 + 0.01 - 0.5

        if user_artist_score[key] > 0:
            user_artists[user_i].append( (art_i, user_artist_score[key]) )  

    user_artist_feat[key] = []
    for i in range(3, len(arr)):
        user_artist_feat[key].append(int(arr[i]))


user_gender = {}
user_age = {}
user_work = {}
user_region = {}
user_music = {}
user_listown = {}
user_listback = {}
user_question = {}

def load_users(p_users):
  for line in open(p_users):
    arr = line.strip().split(",")
    user_i = int(arr[0])

    gender_i = int(arr[1])
    if gender_i > 0:
        user_gender[user_i] = gender_i

    age_i = int(arr[2])
    if age_i >= 72: age_i = 72
    if age_i > 0:
        user_age[user_i] = age_i / 3

    work_i = int(arr[3]) 
    if work_i >= 0:
        user_work[user_i] = work_i

    region_i = int(arr[4])
    if region_i >= 0:
        user_region[user_i] = region_i 

    music_i = int(arr[5])
    if music_i >= 0:
        user_music[user_i] = music_i 

    listown_i = int(float(arr[6]))
    if listown_i >= 0:
        user_listown[user_i] = listown_i 

    listback_i = int(float(arr[7]))
    if listback_i >= 0:
        user_listback[user_i] = listback_i 

    questions = arr[8:27]
    if len(questions) != 19:
        print 'len of questions err:', len(questions)
    user_question[user_i] = {}
    for idx in range( len(questions) ):
        if float(questions[idx]) >= 0:
            user_question[user_i][idx] = float(questions[idx]) / 102.0 + 0.01 - 0.5
  

def mkfeature( path_in, path_out ):
    f_in = open( path_in , 'r' )
    f_out = open( path_out, 'w' )

    max_value_global = 0 
    max_value_user = 0 
    max_value_item = 0 

    for line in f_in:
        feature_list = []

        arr  =  line.strip(' \n').split('\t') #49, 183, 50927, 100, 23        
        user_i  =  int(arr[0].strip())
        art_i  =  int(arr[1].strip())
        track_i  =  int(arr[2].strip())
        month_i = int(arr[3].strip())
        score = int(arr[4].strip())

        #if score < 3: score = 3
        #if score > 97: score = 97

        feature_list_global = []
        feature_list_user = []
        feature_list_item = []


        feature_list_global.append( (art_i, 1) )  #max 50   #14.108->14.105 

        feature_list_global.append( (70 + month_i, 1) ) #max 74  #14.105->14.104

        key = art_i * 100000 + user_i

        if key in user_artist_score:
            feature_list_global.append( (100, user_artist_score[key]) )  #max 100

        if key in user_artist_feat:
            len_word = len(user_artist_feat[key])
            word_weight = math.pow(len_word + 1.0, -0.6)

            for sub_key in user_artist_feat[key]:
                feature_list_global.append( (200 + sub_key, word_weight) )  #max 400

        if user_i in user_gender:
            feature_list_global.append( (1000 + user_gender[user_i] * 100 + art_i, 1) )   #max 1300
            feature_list_global.append( (2000 + user_gender[user_i] * 1000 + track_i, 1) )  #max 5000
        if user_i in user_age:
            feature_list_global.append( (5000 + user_age[user_i] * 100 + art_i, 1) )     #max 8000
            feature_list_global.append( (10000 + user_age[user_i] * 1000 + track_i, 1) )  #max 50000

        feature_list_global.append( (50000 + month_i * 100 + art_i, 1) )  #14.105->14.101

        if user_i in user_work:
            feature_list_global.append( (55000 + user_work[user_i], 1) )  #14.105->14.103

        if user_i in user_region:
            feature_list_global.append( (56000 + user_region[user_i], 1) )  #14.105->14.103

        if user_i in user_music:
            feature_list_global.append( (57000 + user_music[user_i], 1) )  #14.105->14.094

        if user_i in user_listown:
            feature_list_global.append( (58000 + user_listown[user_i], 1) ) #14.09->14.09

        if user_i in user_listback:
            feature_list_global.append( (59000 + user_listback[user_i], 1) ) #14.09->14.08

        if user_i in user_question:
            for sub_key in user_question[user_i]:
                feature_list_global.append( (60000 + sub_key, user_question[user_i][sub_key]) )  #max 60100


        feature_list_user.append( (user_i, 1) )

        feature_list_item.append( (100 + track_i, 1) )

        f_out.write( '%d\t%d\t%d\t%d\t' % ( score, len(feature_list_global), len(feature_list_user), len(feature_list_item) ) )

        for idx in range(len(feature_list_global)):
            f_out.write('%d:%.6f ' % (feature_list_global[idx][0], feature_list_global[idx][1]))
            if feature_list_global[idx][0] > max_value_global: 
                max_value_global = feature_list_global[idx][0]

        for idx in range(len(feature_list_user)):
            f_out.write('%d:%.6f ' % (feature_list_user[idx][0], feature_list_user[idx][1]))
            if feature_list_user[idx][0] > max_value_user: 
                max_value_user = feature_list_user[idx][0]

        for idx in range(len(feature_list_item)):
            if feature_list_item[idx][0] > max_value_item: 
                max_value_item = feature_list_item[idx][0]
            if idx < len(feature_list_item) - 1:
                f_out.write('%d:%.6f ' % (feature_list_item[idx][0], feature_list_item[idx][1]))
            else:
                f_out.write('%d:%.6f\n' % (feature_list_item[idx][0], feature_list_item[idx][1]))

    f_in.close()
    f_out.close()

    print "max global feature value:" + str(max_value_global)
    print "max user factor value:" + str(max_value_user)
    print "max item factor value:" + str(max_value_item)
    print 'generation end'

if __name__ == '__main__':
    import sys
    if len(sys.argv) < 5:
        print 'usage:<input> <output> words users'
        exit(-1)

    path_in = sys.argv[1]
    path_out = sys.argv[2]
    p_words = sys.argv[3]
    p_users = sys.argv[4]

    import gc
    gc.disable()

    load_words(p_words)
    load_users(p_users)
    mkfeature( path_in, path_out )

