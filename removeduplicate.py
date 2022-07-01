import os
import time
from colorama import Back, Style, Fore

linux = 'clear'
windows = 'cls'
os.system([linux,windows][os.name == 'nt'])

banner = '''

     ┏━━━┓╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋┏━━━┓╋╋╋╋╋┏┓╋╋╋╋╋╋╋┏┓
     ┃┏━┓┃╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋┗┓┏┓┃╋╋╋╋╋┃┃╋╋╋╋╋╋┏┛┗┓
     ┃┗━┛┣━━┳┓┏┳━━┳┓┏┳━━┓╋┃┃┃┣┓┏┳━━┫┃┏┳━━┳━┻┓┏╋━━┓
     ┃┏┓┏┫┃━┫┗┛┃┏┓┃┗┛┃┃━┫╋┃┃┃┃┃┃┃┏┓┃┃┣┫┏━┫┏┓┃┃┃┃━┫
     ┃┃┃┗┫┃━┫┃┃┃┗┛┣┓┏┫┃━┫┏┛┗┛┃┗┛┃┗┛┃┗┫┃┗━┫┏┓┃┗┫┃━┫
     ┗┛┗━┻━━┻┻┻┻━━┛┗┛┗━━┛┗━━━┻━━┫┏━┻━┻┻━━┻┛┗┻━┻━━┛
     ╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋┃┃
     ╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋┗┛
                                          
              By : Wan5550
              Github : github.com/wannazid
              Blog : www.malastech.my.id
'''

hijau = Fore.GREEN
merah = Fore.RED
cyan = Fore.CYAN
tai = Fore.YELLOW
biru = Fore.BLUE
batas = Style.RESET_ALL

print(tai)
print(banner)
print(batas)

print(hijau)
input_list = input('[#] List Duplicate > ')
input_save = input('[#] Result Name > ')
print(batas)

kosong = []
f = open(input_list,"r").read().splitlines()
for ls in f:
    if ls not in kosong:
        kosong += [ls]
    else:
        pass
open(input_list,"w").write("")
for ls in kosong:
    open(input_list,"a").write(ls+"\n")
    os.remove(input_list)
    open(input_save,'a').write(ls+'\n')
text = '[!] Done remove duplicate and saving !'
for huruf in text:
	print(huruf,end='',flush=True)
	time.sleep(0.3)
print('\n')
