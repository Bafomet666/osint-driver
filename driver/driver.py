# Легкий и понятный код по устанвоке зависимостей

import os

page_1 = fr'''


  _____     ______     __     __   __   ______     ______    
 /\  __-.  /\  == \   /\ \   /\ \ / /  /\  ___\   /\  == \   
 \ \ \/\ \ \ \  __<   \ \ \  \ \ \'/   \ \  __\   \ \  __<   
  \ \____-  \ \_\ \_\  \ \_\  \ \__|    \ \_____\  \ \_\ \_\ 
   \/____/   \/_/ /_/   \/_/   \/_/      \/_____/   \/_/ /_/ 
                                                            

 Установка pycurl, geckodriver + selenium, vlc
 
 driver osintsan pro 5+
 
 [ version 1.0 ]
'''


def driver():
    print(' Установка pycurl')
    os.system('sudo apt install libcurl4-gnutls-dev librtmp-dev')
    os.system('sudo apt-get install libcurl4-gnutls-dev librtmp-dev')
    os.system('pip3 install setuptools')
    os.system('pip3 install pycurl')
    os.system('pip3 install grab')
   
    print(' Установка webdriver')
    os.system('sudo chmod +x /usr/local/bin/geckodriver')
    os.system('sudo mv geckodriver /usr/local/bin/geckodriver')
    os.system('sudo chown root:root /usr/local/bin/geckodriver')
    
    print(' Установка vlc')
    os.system('pip3 install python-vlc')
    os.system('sudo apt-get install vlc')
    print(' \nУстановка завершена')
    os.system('exit')
    
driver()
