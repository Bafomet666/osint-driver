# Легкий и понятный код по установке зависимостей, сделано для новичков.

WHSL = C = "\033[39m"
REDL = R = "\033[0;31m"
GNSL = G = "\033[1;34m"
GRNL = U = "\033[32;1m"
FIOL = H = "\033[95m"

page_1 = fr'''{GRNL}
  ______             _                          _______                __       
 |_   _ `.          (_)                        |_   __ \              [  |  _   
   | | `. \ _ .--.  __  _   __  .---.  _ .--.    | |__) |,--.   .---.  | | / ]  
   | |  | |[ `/'`\][  |[ \ [  ]/ /__\\[ `/'`\]   |  ___/`'_\ : / /'`\] | '' <   
  _| |_.' / | |     | | \ \/ / | \__., | |      _| |_   // | |,| \__.  | |`\ \  
 |______.' [___]   [___] \__/   '.__.'[___]    |_____|  \'-;__/'.___.'[__|  \_] 
                                                                               
 {WHSL}Driver Pack on {REDL}OSINT-SAN PRO
 
 {WHSL}Данный pack драйверов подходит под многих осинт инструментов,
 {WHSL}связанных с парсингом данных
 
 Перед запуском модулей советую запустить терминал от рута
 Командой:{REDL} sudo su
 
 {REDL}[ {GNSL}Version 1.3 {REDL}]
 
 {REDL}[ {GNSL}1 {REDL}]  {WHSL}Установка {GNSL}pycurl and grub                   {REDL}[ {GNSL}5 {REDL}]  {WHSL}Написать {GNSL}разработчику
 
 {REDL}[ {GNSL}2 {REDL}]  {WHSL}Установка {GNSL} geckodriver                      {REDL}[ {GNSL}6 {REDL}]  {WHSL}Установить {GNSL}selenium
 
 {REDL}[ {GNSL}3 {REDL}]  {WHSL}Основные зависимости                        {REDL}[ {GNSL}7 {REDL}]
 
 {REDL}[ {GNSL}4 {REDL}]  {WHSL}Покинуть, очистить процессы
 
'''


def driver():
    import webbrowser
    import os

    os.system("printf '\033]2;Driver pack 1.3 📥 \a'")
    os.system("clear")
    print(page_1)
    while True:
        try:
            option = input(f"{REDL} └──> {WHSL} Выберите опцию:{GNSL} ")
        except KeyboardInterrupt:
            return

        if option == '1':
            os.system('sudo apt install libcurl4-gnutls-dev librtmp-dev')
            os.system('sudo apt-get install libcurl4-gnutls-dev librtmp-dev')
            os.system('pip3 install setuptools')
            os.system('pip3 install pycurl')
            os.system('pip3 install grab')
            os.system("clear")
            print(page_1)
            print(' \n Установка прошла успешно\n')

        elif option == '2':
            os.system(
                'wget https://github.com/mozilla/geckodriver/releases/download/v0.30.0/geckodriver-v0.30.0-linux64.tar.gz')
            os.system('sudo tar -xvzf geckodriver-v0.30.0-linux64.tar.gz')
            os.system('sudo chmod +x /usr/local/bin/geckodriver')
            os.system('sudo mv geckodriver /usr/local/bin/geckodriver')
            os.system('sudo chown root:root /usr/local/bin/geckodriver')

        elif option == '3':
            os.system('sudo pip3 install -r requirements.txt')
            os.system("clear")
            print(page_1)
            print(' \n Установка прошла успешно\n')

        elif option == '4':
            os.system('pkill -9 -f driver.py')

        elif option == '5':
            urls = [
                "https://t.me/satana666mx",
            ]
            for url in urls:
                webbrowser.open(url)
            print(f"\n Сайты открыты")

        elif option == '6':
            page_2 = f''' Друг я пока еще не проработал эту функцию в автомат
                      Перейди по ссылкам там гайд
                      
                      https://tecadmin.net/setup-selenium-with-chromedriver-on-debian/
                      https://bytetell.com/123/
                      https://losst.ru/ustanovka-selenium-v-linux '''
            os.system("clear")
            print(page_1)
            print(page_2)


driver()
