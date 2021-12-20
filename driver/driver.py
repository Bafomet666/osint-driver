# Легкий и понятный код по устанвоке зависимостей

import os

FIOL = H = "\033[95m"
REDL = R = "\033[0;31m"

page_1 = fr'''{FIOL}


  _____     ______     __     __   __   ______     ______    
 /\  __-.  /\  == \   /\ \   /\ \ / /  /\  ___\   /\  == \   
 \ \ \/\ \ \ \  __<   \ \ \  \ \ \'/   \ \  __\   \ \  __<   
  \ \____-  \ \_\ \_\  \ \_\  \ \__|    \ \_____\  \ \_\ \_\ 
   \/____/   \/_/ /_/   \/_/   \/_/      \/_____/   \/_/ /_/ 
                                                            
{REDL}
 Установка pycurl, geckodriver + selenium, vlc
 
 driver osintsan pro 5+
 
 [ version 1.0 ]
'''


def driver():
    os.system('clear')
    print(page_1)
    print(f'{REDL} \n Установка pycurl\n{FIOL}')
    os.system('sudo apt install libcurl4-gnutls-dev librtmp-dev')
    os.system('sudo apt-get install libcurl4-gnutls-dev librtmp-dev')
    os.system('pip3 install setuptools')
    os.system('pip3 install pycurl')
    os.system('pip3 install grab')
   
    print(f'{REDL} \n Установка webdriver\n{FIOL}')
    os.system('sudo chmod +x /usr/local/bin/geckodriver')
    os.system('sudo mv geckodriver /usr/local/bin/geckodriver')
    os.system('sudo chown root:root /usr/local/bin/geckodriver')
    print(f' {REDL} \n Установлено')
    
    print(f'{REDL} \n Установка vlc\n{FIOL}')
    os.system('pip3 install python-vlc')
    os.system('sudo apt-get install vlc')
    print(f'{REDL} \n Установка завершена')
    os.system('exit')
    
driver()
