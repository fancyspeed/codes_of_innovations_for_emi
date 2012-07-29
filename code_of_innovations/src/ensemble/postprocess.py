import sys
import math


def main(p_input, p_output, p_art_uid, p_uid, p_user_rate):

    art_uid_avescore = {}
    art_uid_maxscore = {}
    art_uid_minscore = {}
    art_uid_num  = {}

    for line in open(p_art_uid):
        artid, uid, ave_score, min_score, max_score, score_num = line.strip().split('\t')
        art_uid_avescore[artid+'-'+uid] = float(ave_score)
        art_uid_minscore[artid+'-'+uid] = float(min_score)
        art_uid_maxscore[artid+'-'+uid] = float(max_score)
        art_uid_num[artid+'-'+uid] = float(score_num)

    infile = open(p_input)
    outfile_final = open(p_output, 'w')
    outfile_final.write(infile.readline())

    for line in infile:
        artid, iid, uid, score, time = line.strip().split(',')
        score = float(score)   
        key = artid + '-' + uid

        newscore = score

        if key in art_uid_num and art_uid_num[key] <= 3:
            outfile_final.write( str(artid)+","+str(iid)+","+str(uid)+","+str(newscore)+","+str(time)+"\n" )
            continue       

        if key in art_uid_minscore and  score < art_uid_minscore[key] - 5:
#            print 'min:', score,art_uid_minscore[key]
            newscore = score * 0.7 + art_uid_minscore[key] * 0.3
        if key in art_uid_maxscore and score  > art_uid_maxscore[key] + 5:
#            print 'max:', score , art_uid_maxscore[key]
            newscore = score * 0.7 + art_uid_maxscore[key] * 0.3

        outfile_final.write( str(artid)+","+str(iid)+","+str(uid)+","+str(newscore)+","+str(time)+"\n" ) 
    
if __name__ == "__main__":
    import sys
    if len(sys.argv) < 6:
        print '<usage> input output art_uid_average uid_average user_rate_stat'
        exit(-1) 
    p_input = sys.argv[1]
    p_output = sys.argv[2]
    p_art_uid = sys.argv[3]
    p_uid = sys.argv[4]
    p_user_rate = sys.argv[5]

    main(p_input, p_output, p_art_uid, p_uid, p_user_rate)

