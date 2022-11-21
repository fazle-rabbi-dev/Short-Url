# Author: Fazle Rabbi
# Date: 21 November, 2022
# Warning: Don't copy my code without my permission.
# ** [Changing Credit/Copying Code] Don't Made You A Coder.
# ** This code is open source, so that anyone can read this code and gain some knowledge.
import os,sys,time,requests,json
import urllib.request
from doShortUrl import *


# Clear Terminal:
def clear():
   os.system('clear')

os.system('termux-reload-settings')
clear()


# Colors
rd='\033[1;91m'
gr='\033[1;92m'
yl='\033[1;93m'
bl='\033[1;94m'
pr='\033[1;95m'
cn='\033[1;96m'
rs='\033[0m'
optionColor='\033[1;95m'
optionNumberColor='\033[1;95m'

# Check Device Internet Connection:
def isOnline(host='http://google.com'):
    try:
        urllib.request.urlopen(host) #Python 3.x
        return True
    except:
        return False

# test
# print( "connected" if connect() else "no internet!" )


# Banner
def banner():
   print(f"""
{cn} ___  _               _     _ _       _ 
{bl}/ __>| |_  ___  _ _ _| |_  | | | _ _ | |
{gr}\__ \| . |/ . \| '_> | |   | ' || '_>| |
{pr}<___/|_|_|\___/|_|   |_|   `___'|_|  |_|{rs}
                                                                    
   
   >>> Device {rd}{'ONLINE' if isOnline() else 'OFFLINE'}{rs}
   
   >>>{gr} Coded By Fazle Rabbi{rs}
   >>>{bl} Github:https://github.com/fh-rabbi{rs}
   >>>{pr} V1.0.0{rs}
   """)

# Main Menu
def menu():
   print(f"""
   `-`-`-`-`-`-`-`-`-``-`-`-`-`
   |                          |
   | {optionNumberColor}1{rs} ➡ {optionColor}Short Your Url{rs}       |
   | {optionNumberColor}2{rs} ➡ {optionColor}About This Tool{rs}      |
   | {optionNumberColor}3{rs} ➡ {optionColor}About Author{rs}         |
   | {optionNumberColor}4{rs} ➡ {optionColor}More Tools{rs}           |
   | {optionNumberColor}5{rs} ➡ {optionColor}Check Update{rs}         |
   | {optionNumberColor}0{rs} ➡ {optionColor}Exit{rs}                 |
   |                          |
   `-`-`-`-``-`-`-`-``-`-`-`-`
   """)
   option=input(f"   [*] {gr}Choose An Option:")
   if option == '1':
      shortUrl()
   elif option == '0':
      clear()
      print(f'{rd}🚀 Quiting...')
      print(f"{yl}Hey 🖐️,Thanks for using this tool.")
      # time.sleep(1)
      os.system('exit 0')
   else:
      print('')
      print(f'{rd}   [*] Oops! Wrong Option{rs}')
      time.sleep(1)
      clear()
      time.sleep(.5)
      banner()
      menu()
      
# ulr Shortner Logic:
def shortUrl():
   os.system('clear')
   # time.sleep(1)
   url=str(input(f"{rs}[*] Enter Your Full Url:{gr}"))
   if 'http' in url:
      doShortUrl(url)
   else:
      print(rd+"[*] Invalid URL"+rs)
      time.sleep(1)
      popUp(url)


def doShortUrl(url):
   hasInternet = isOnline()
   print(f"{rs}[*] {rd}Checking internet connection...{rs}")
   time.sleep(1)
   if hasInternet:
      print(f"[*] {gr}Internet connection Ok...{rs}")
      time.sleep(1)
      print(f"[*] {bl}Url Checking...{rs}")
      # Url Validation:
      try:
         request=requests.get(url)
         # print(request.status_code)
         # print(request)
         time.sleep(1)
         if request.status_code:
            print(f"[*] {yl}Url valid...{rs}")
            time.sleep(1)
            print(f"[*] {pr}Url Shorting Please Wait...{rs}")
            # Calling api for Short Url:
            data=getData('https://github.com/fh-rabbi')
            print('')
            print("🎉 URL Shorten Successfull.")
            print('')
            print(f"[*] Full URL:{yl}{data['fullUrl']}{rs}")
            print(f"[*] Short URL:{yl}https{data['shortUrl'][4:]}{rs}")
            print('')
            print(f"🚨 Press {cn}any key{rs} for short another url, or press {cn}(m){rs} for Main Menu.")
            print('')
            opt=input(f"{rs}🚀>>{cn}")
            if opt == 'M' or opt == 'm':
               clear()
               time.sleep(1)
               banner()
               menu()
            else:
               clear()
               shortUrl()
         else:
            pass
      except:
         print(f'[*] {rd}Oops! Invalid Url!')
         time.sleep(1)
         popUp(url);
   else:
      print(f"{rd}[*] Internet connection Problem...")
      time.sleep(1)
      popUp(url)
      
# popUp Menu
def popUp(url):
   os.system('clear')
   opt=input(f"""{rs}
   [{cn}B{rs}] {pr}Go Back{rs}
   [{cn}M{rs}] {pr}Go Main Menu{rs}
   [{cn}*{rs}] {yl}Choose An Option:{cn}""")
   if opt == 'B' or opt == 'b':
      clear()
      time.sleep(1)
      shortUrl()
   elif opt == 'M' or opt == 'm':
      os.system('clear')
      banner()
      menu()
   else:
      print(rd+'[*] wrong option')
      popUp()


# Call The Function:
clear()
banner()
menu()
