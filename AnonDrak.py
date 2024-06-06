#!/usr/bin/env python3
# Author: Maxim3lian

from __future__ import print_function
import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from termcolor import colored
from random import choice
from multiprocessing.dummy import Pool as ThreadPool
from colorama import init, Fore, Style
from datetime import datetime, timedelta
import re

init(autoreset=True)

def grab_defacer_net(first_page, last_page):
    url_template = 'https://defacer.net/archive/{}'
    urls = []
    for page in range(first_page, last_page+1):
        url = url_template.format(page)
        response = requests.get(url)
        html_content = response.text
        soup = BeautifulSoup(html_content, 'html.parser')
        for text in soup.stripped_strings:
            if '.' in text:
                if not text.startswith('http://') and not text.startswith('https://'):
                    text = 'http://' + text
                parsed_url = urlparse(text)
                domain_name = parsed_url.netloc.split(':')[0]
                domain_parts = domain_name.split('.')
                if len(domain_parts) >= 2:
                    tld = domain_parts[-1]
                    if len(tld) <= 3:
                        domain_name = '.'.join(domain_parts[-2:])
                    else:
                        domain_name = '.'.join(domain_parts[-3:])
                if domain_name not in urls:
                    urls.append(domain_name)
                    print('\n\t\t[+] Grabbed : {}'.format(domain_name))
    with open('Grabbed.txt', 'w') as file:
        for url in urls:
            file.write(url + '\n')
    print('\n\t\t[!] MaVanNam WAS HERE [!]')

def grab_wordpress_themes(themename, themepages):
    for page in range(1, int(themepages) + 1):
        state = ['us1', 'us2', 'us3', 'us4', 'us5', 'us6', 'us7', 'us8', 'us9', 'us10', 'us11', 'us12', 'us13', 'us14', 'us15', 'eu1', 'eu2', 'eu3', 'eu4', 'eu5', 'eu6', 'eu7', 'eu8', 'eu9', 'eu10']
        proxy = choice(state)
        ua = {
            'Origin': 'https://' + proxy + '.proxysite.com',
            'Upgrade-Insecure-Requests': '1',
            'Referer': 'https://' + proxy + '.proxysite.com/process.php?d=d5ww0usE5q1XyjorWQH7sw%3D%3D&b=1&f=norefer',
            'Content-Type': 'application/x-www-form-urlencoded',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 7.0; SM-G892A Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Mobile Safari/537.36'
        }
        data = {'allowCookies': 'on', 'd': 'https://themetix.com/' + themename + '/' + str(page)}
        test = requests.post('https://' + proxy + '.proxysite.com/includes/process.php?action=update', data=data, headers=ua, timeout=10)
        if 'site' in test.content.decode('utf-8'):
            print('\n\t\t[!] Contact : t.me/Maxim3lian_Channel [!]')
            domains = re.findall(r'<p style="margin-bottom: 20px">(.*?)</p>', test.content.decode('utf-8'))
            with open('Grabbed.txt', 'a') as file:
                for domain in domains:
                    print('\n\t\t[+] Grabbed : ' + domain)
                    file.write('http://' + domain + '\n')

def grab_zone_xsec(first_page, last_page):
    url_template = 'https://zone-xsec.com/archive/page={}'
    urls = []
    for page in range(first_page, last_page+1):
        url = url_template.format(page)
        response = requests.get(url)
        html_content = response.text
        soup = BeautifulSoup(html_content, 'html.parser')
        for text in soup.stripped_strings:
            if '.' in text:
                if not text.startswith('http://') and not text.startswith('https://'):
                    text = 'http://' + text
                parsed_url = urlparse(text)
                domain_name = parsed_url.netloc.split(':')[0]
                domain_parts = domain_name.split('.')
                if len(domain_parts) >= 2:
                    tld = domain_parts[-1]
                    if len(tld) <= 3:
                        domain_name = '.'.join(domain_parts[-2:])
                    else:
                        domain_name = '.'.join(domain_parts[-3:])
                if domain_name not in urls:
                    urls.append(domain_name)
                    print('\n\t\t[+] Grabbed : {}'.format(domain_name))
    with open('Grabbed.txt', 'w') as file:
        for url in urls:
            file.write(url + '\n')
    print('\n\t\t[!] MaVanNam WAS HERE [!]')

def main():
    print('''
    
╔═══╗────────────────────────╔═══╗────╔╗
║╔═╗║────────────────────────╚╗╔╗║────║║
║║─║╠═╗╔══╦═╗╔╗─╔╦╗╔╦══╦╗╔╦══╗║║║╠═╦══╣║╔╗
║╚═╝║╔╗╣╔╗║╔╗╣║─║║╚╝║╔╗║║║║══╣║║║║╔╣╔╗║╚╝╝
║╔═╗║║║║╚╝║║║║╚═╝║║║║╚╝║╚╝╠══╠╝╚╝║║║╔╗║╔╗╗
╚╝─╚╩╝╚╩══╩╝╚╩═╗╔╩╩╩╩══╩══╩══╩═══╩╝╚╝╚╩╝╚╝
─────────────╔═╝║
─────────────╚══╝ 
       Price => 350k
       Twitter : Anon1995_Ops
       Telegram : Cyber1995_Xn [Ma Văn Nam]''')

    first_page = int(input('\n\t[>] Enter the first page number: '))
    last_page = int(input('\n\t\t[>] Enter the last page number: '))
    themename = input('\n\t[>] Theme Name: ')
    themepages = input('\n\t[>] N.O.P: ')

    thread_pool = ThreadPool(3)
    thread_pool.apply_async(grab_defacer_net, args=(first_page, last_page))
    thread_pool.apply_async(grab_wordpress_themes, args=(themename, themepages))
    thread_pool.apply_async(grab_zone_xsec, args=(first_page, last_page))

    thread_pool.close()
    thread_pool.join()

if __name__ == "__main__":
    main()
