#coding=utf-8
#Author: Zhang Yuhui
#Tel: (+86)185-3888-2881
#Email: yuhui-zh15@mails.tsinghua.edu.cn
#Introduction: Get followerscount and name data produced by 'merge.py'

import time
import os

userdata = dict()
filelist = [
'data1.txt',
'data2.txt',
'data3.txt',
'data4.txt',
'data5.txt',
'data6.txt'
]

statistic_file = '/data/disk5/private/weibodata/filename/statistics_all.csv'
srcpath = '/data/disk5/private/weibodata/user/'

with open(statistic_file) as fin:
	print fin.readline()
	for line in fin:
		splitline = line.split(',')
		uid = int(splitline[0])
		postnum = int(splitline[1])
		keywordsnum = int(splitline[2])
		ratio = float(splitline[3])
		userdata[uid] = [postnum, keywordsnum, ratio, 0, '']

ferr = open('error_details.txt', 'w')
for filename in filelist:
	if (os.path.isfile(srcpath + filename) == False): continue
	print('Now time = ' + time.asctime() + ', Processing ' + filename + '...')
	with open(srcpath + filename) as fin:
		for line in fin:
			try:
				jsonline = json.loads(line)
				uid = jsonline['id']
				name = jsonline['screen_name']
				followerscount = jsonline['followers_count']
				if uid not in userdata:
					userdata[uid][3] = followerscount
					userdata[uid][4] = name
			except:
				ferr.write(filename + '\t' + line)	
ferr.close()

fout = open('statistics_details.csv', 'w')
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

		
