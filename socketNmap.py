# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 18:45:51 2023

@author: alpar
"""

import socket 
import re
import sys
from colorama import init, Fore
from termcolor import colored
#192.168.56.1 host ip address
class AnneniSikimHatası(Exception):
    "anneni siktim öldü"
    pass


def ipformat(target):
    match = re.match(r"[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}",target)
    
    if bool(match):
            print("ip format is True")
            return True
    else:
        print("ip format is False")
        
def portformat(portrange):
    
    match = re.match("([0-9]+)-([0-9]+)", portrange)
    if bool(match):
        print("port format is correct")
        minimumport,maximumport = re.split("-",portrange)
        return [minimumport,maximumport]
    else:
        print("port format is incorrect")
        return False
    
def IsPortOpen(target,port):
    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
        socket.setdefaulttimeout(0.1)
        try:
            s.connect((target,port))
        except:
            return False
        else:
            return True
 
    
    
def main():
    print("please enter an ip address: (enter q to quit)")
    targetIp = input()
    
    if targetIp=="q":
        sys.exit(0)
    
    init()
    
    RED = Fore.RED
    RESET = Fore.RESET
    
    #host = "151.101.1.69"
    ipformat(targetIp)    
    print("please enter range of port number: [minimum port range]-[maximum port range]")
    portrange = input()
    
    
    minimumPort,maximumPort=portformat(portrange)

    
    for i in range(int(minimumPort),int(maximumPort)+1):
        if  IsPortOpen(targetIp, i):
            print(f"{RED}[+] {targetIp}: {i} is open {RESET}")
    
        


while(1):
    main()

#%%
a=socket.gethostbyname("www.stackoverflow.com")
print(a)
a = input()
with socket.socket(socket.AF_INET,socket.SOCK_STREAM)  as s:
    for i in range(1,120):
        result =s.connect_ex((a,i))
        if result ==0:
            print(f"port {i} is open")