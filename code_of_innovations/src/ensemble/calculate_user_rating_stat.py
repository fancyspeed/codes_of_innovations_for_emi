import math
import sys


def main(p_train, p_output):

    infile = open(p_train)
    infile.readline()

    uid_score = {}

    for line in infile:
        artid, iid, uid, score, time = line.strip().split(',')

        if uid not in uid_score:
            uid_score[uid] = []

        uid_score[uid].append(float(score) )


    outfile = open(p_output, 'w')
    for key in uid_score:

        score_list = sorted(uid_score[key])

        total = 0.0
        for member in score_list: 
            total += member

        mean_score = total / len(score_list)

        mid_score = score_list[len(score_list)/2]

        var = 0.0
        for member in score_list:
            var += (member - mean_score) * (member - mean_score)
        var /= len(score_list)
        
        #uid, num, mean_score, mid_score, var_score
        outfile.write(key + '\t' + str(len(score_list)) + '\t' + str(mean_score) + '\t' + str(mid_score) + '\t' + str(var) + '\n')

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


