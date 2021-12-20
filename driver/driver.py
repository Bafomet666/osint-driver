# Легкий и понятный код по устанвоке зависимостей

import os

page_1 = fr'''

 _____     ______     __     __   __   ______     ______    
/\  __-.  /\  == \   /\ \   /\ \ / /  /\  ___\   /\  == \   
\ \ \/\ \ \ \  __<   \ \ \  \ \ \'/   \ \  __\   \ \  __<   
 \ \____-  \ \_\ \_\  \ \_\  \ \__|    \ \_____\  \ \_\ \_\ 
  \/____/   \/_/ /_/   \/_/   \/_/      \/_____/   \/_/ /_/ 
                                                            


'''


def driver():
    print(' Установка pycurl')
    os.system('sudo apt install libcurl4-gnutls-dev librtmp-dev sudo apt-get install libcurl4-gnutls-dev librtmp-dev pip3 install setuptools pip3 install pycurl pip3 install grab')
    os.system('sudo su')
    print(' Установка webdriver')
    os.system('sudo chmod +x /usr/local/bin/geckodriver')
    os.system('sudo mv geckodriver /usr/local/bin/geckodriver')
    os.system('sudo chown root:root /usr/local/bin/geckodriver')
    os.system('wget https://selenium-release.storage.googleapis.com/3.141/selenium-server-standalone-3.141.59.jar')
    os.system('sudo java -jar selenium-server-standalone-3.141.59.jar')
    print(' Установка vlc')
    os.system('pip3 install python-vlc')
    os.system('sudo apt-get install vlc')
    
    
driver()
    
    
