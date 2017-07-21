#coding=utf-8
#Author: Zhang Yuhui
#Tel: (+86)185-3888-2881
#Email: yuhui-zh15@mails.tsinghua.edu.cn
#Introduction: Do statistics in AllWeibo Database, 'statistics.csv' stores results(uid, postnum, keywordsnum, ratio)

import json
import os
import sys

keywords = set()
userdata = dict()
with open('seedwords.txt') as fin:
	line = fin.readline()
	splitline = line.split(',')
	for keyword in splitline:
		keywords.add(keyword)

#filelist = ['microblogs0.txt', 'microblogs1.txt', 'microblogs2.txt', 'microblogs3.txt', 'microblogs4.txt', 'microblogs5.txt', 'microblogs6.txt', 'microblogs7.txt', 'microblogs8.txt', 'microblogs9.txt', 'microblogs10.txt', 'microblogs11.txt', 'microblogs12.txt', 'microblogs13.txt']
filelist = ['dump1_microblogs_1KW_4.lzo']
srcpath = '/data/disk5/hadoop_backup/user/kuangchong/allweibodata/microblog/'
dstpath = '/data/disk5/private/weibodata/'

ferr = open('error.txt', 'w')
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
				text = jsonline['text']
				if uid not in userdata:
					userdata[uid] = [0, 0]
				keywordsnum = 0
				for keyword in keywords:
					if text.find(keyword) != -1:
						keywordsnum += 1
				userdata[uid][0] += 1
				userdata[uid][1] += keywordsnum
				print userdata[uid]
				raw_input()
			except:
				ferr.write(line)	
				pass
	os.system('rm ' + dstpath + unzipfilename)
ferr.close()

fout = open('statistics.csv', 'w')
fout.write('uid,postnum,keywordsnum,ratio\n')
for user in userdata.items():
	uid = user[0]
	postnum = user[1][0]
	keywordsnum = user[1][1]
	#ratio = 1.0 * keywordsnum / postnum
	#fout.write(str(uid) + ',' + str(postnum) + ',' + str(keywordsnum) + ',' + str(ratio) + '\n')
	fout.write(str(uid) + ',' + str(postnum) + ',' + str(keywordsnum) + '\n')
fout.close()

		
