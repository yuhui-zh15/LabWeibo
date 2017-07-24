#coding=utf-8
#Author: Zhang Yuhui
#Tel: (+86)185-3888-2881
#Email: yuhui-zh15@mails.tsinghua.edu.cn
#Introduction: Get following and nickname data produced by 'merge.py'

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

srcpath = '/data/disk5/private/weibodata/user/'

ferr = open('error_merge.txt', 'w')
for filename in filelist:
	if (os.path.isfile(srcpath + filename) == False): continue
	print('Now time = ' + time.asctime() + ', Processing ' + filename + '...')
	with open(srcpath + filename) as fin:
		for line in fin:
			try:
				splitline = line.split(',')
				uid = int(splitline[0])
				postnum = int(splitline[1])
				keywordsnum = int(splitline[2])
				if uid not in userdata:
					userdata[uid] = [0, 0]
				userdata[uid][0] += postnum
				userdata[uid][1] += keywordsnum
			except:
				ferr.write(filename + '\t' + line)	
ferr.close()

fout = open('statistics_all.csv', 'w')
fout.write('uid,postnum,keywordsnum,ratio\n')
for user in userdata.items():
	uid = user[0]
	postnum = user[1][0]
	keywordsnum = user[1][1]
	ratio = 1.0 * keywordsnum / postnum
	fout.write(str(uid) + ',' + str(postnum) + ',' + str(keywordsnum) + ',' + str(ratio) + '\n')
fout.close()

		
