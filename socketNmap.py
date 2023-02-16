# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 18:45:51 2023

@author: alpar

meh
meh meh


"""

import socket 
import re
import sys
from colorama import init, Fore
from termcolor import colored
from concurrent.futures import ThreadPoolExecutor

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
        socket.setdefaulttimeout(3)
        try:
            s.connect((target,port))
        except:
            return False
        else:
            return True
        
def portscan(host,ports):
    
    init()
    
    GREEN = Fore.GREEN
    RESET = Fore.RESET
    
    print("scanning for open ports ...")
    with ThreadPoolExecutor(len(ports)) as executor:
        
        results = executor.map(IsPortOpen,[host]*len(ports),ports)
        
        for port,is_open in zip(ports,results):
            
            if is_open:
                print(f"{GREEN}[+]{host} : port {port} open {RESET}")
 
    
    
def main():
    print("please enter an ip address: (enter q to quit)")
    targetIp = input()
    
    if targetIp=="q":
        sys.exit(0)
    
    #host = "151.101.1.69"
    ipformat(targetIp)    
    print("please enter range of port number: [minimum port range]-[maximum port range]")
    portrange = input()
    
    
    minimumPort,maximumPort=portformat(portrange)
    ports =[i for i in range(int(minimumPort),int(maximumPort)+1)]
    
    portscan(targetIp, ports)
    



while(1):
    main()
