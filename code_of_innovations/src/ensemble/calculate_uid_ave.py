import math
import sys


def main(p_train, p_output):

    infile = open(p_train)
    infile.readline()

    art_uid_score = {}
    uid_score = {}


    for line in infile:
        artid, iid, uid, score, time = line.strip().split(',')

    
        if uid not in uid_score:
            uid_score[uid] = []

        uid_score[uid].append(float(score) )


    outfile = open(p_output, 'w')
    for key in uid_score:

        max_score = max(uid_score[key])
        min_score = min(uid_score[key])
        total = 0
        for member in uid_score[key]:
            total += member
        
        #uid, ave_score, min_score, max_score, score_num
        outfile.write(key + '\t' + str(float(total)/len(uid_score[key])) + '\t' + str(min_score) + '\t'+str(max_score) + '\t' + str(len(uid_score[key])) + '\n')

    outfile.close()
    infile.close()


if __name__ == '__main__':
    import sys
    if len(sys.argv) < 3:
        print '<usage> train output'
        exit(-1)
    p_train = sys.argv[1]
    p_output = sys.argv[2]

    main(p_train, p_output)


