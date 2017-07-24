#coding=utf-8
#Author: Zhang Yuhui
#Tel: (+86)185-3888-2881
#Email: yuhui-zh15@mails.tsinghua.edu.cn
#Introduction: Filt users according to followerscount produced by 'detail.py'

import sys

userdata = dict()
statistic_file = '/data/disk5/private/weibodata/filelist/statistics_details.csv'

if (len(sys.argv) != 2):
	print('Error argv')
	exit(-1)

THRESHOLD = int(sys.argv[1])

with open(statistic_file) as fin:
	fin.readline()
	for line in fin:
		splitline = line.strip().split(',')
		uid = int(splitline[0])
		postnum = int(splitline[1])
		keywordsnum = int(splitline[2])
		ratio = float(splitline[3])
		followerscount = int(splitline[4])
		name = str(splitline[5])
		if (followerscount >= THRESHOLD):
			userdata[uid] = [postnum, keywordsnum, ratio, followerscount, name]

fout = open('statistics_leader.csv', 'w')
fout.write('uid,postnum,keywordsnum,ratio,followerscount,name\n')
for user in userdata.items():
	uid = user[0]
	postnum = user[1][0]
	keywordsnum = user[1][1]
	ratio = user[1][2]
	followerscount = user[1][3]
	name = user[1][4]
	fout.write(str(uid) + ',' + str(postnum) + ',' + str(keywordsnum) + ',' + str(ratio) + ',' + str(followerscount) + ',' + str(name) + '\n')
fout.close()
		
