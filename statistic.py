#coding=utf-8
#Author: Zhang Yuhui
#Tel: (+86)185-3888-2881
#Email: yuhui-zh15@mails.tsinghua.edu.cn
#Introduction: Do statistics in AllWeibo Database, 'statistics.csv' stores results(uid, postnum, keywordsnum, ratio)

import json
import os
import sys

if len(sys.argv) != 2:
	print 'Error!'
	exit(-1)

keywords = list()
userdata = dict()
with open('seedwords.txt') as fin:
	line = fin.readline()
	splitline = line.split(',')
	for keyword in splitline:
		keywords.append(keyword)

filelist = list()
with open(sys.argv[1]) as fin:
	for line in fin:
		filelist.append(line.strip())
srcpath = '/data/disk5/hadoop_backup/user/kuangchong/allweibodata/microblog/'
dstpath = '/data/disk5/private/weibodata/'

ferr = open('error_' + sys.argv[1] + '.txt', 'w')
for filename in filelist:
	print('Unzip ' + filename + '...')
	os.system('lzop -d ' + srcpath + filename + ' -p' + dstpath)
	unzipfilename = filename.split('.')[0]
	with open(dstpath + unzipfilename) as fin:
		print('Processing ' + unzipfilename + '...')
		for line in fin:
			try:
				jsonline = json.loads(line)
				uid = jsonline['user_id']
				text = jsonline['text'].encode('utf-8')
				if uid not in userdata:
					userdata[uid] = [0, 0]
				keywordsnum = 0
				for keyword in keywords:
					if text.find(keyword) != -1:
						keywordsnum += 1
				userdata[uid][0] += 1
				userdata[uid][1] += keywordsnum
			except:
				ferr.write(line)	
	os.system('rm ' + dstpath + unzipfilename)
ferr.close()

fout = open('statistics_' + sys.argv[1] + '.csv', 'w')
fout.write('uid,postnum,keywordsnum,ratio\n')
for user in userdata.items():
	uid = user[0]
	postnum = user[1][0]
	keywordsnum = user[1][1]
	ratio = 1.0 * keywordsnum / postnum
	fout.write(str(uid) + ',' + str(postnum) + ',' + str(keywordsnum) + ',' + str(ratio) + '\n')
fout.close()

		
