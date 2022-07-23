import random
import os

def mac_spoof():
    default=os.system("ipconfig | grep ether")
    print(f"Your actual Mac- Adress is: {default}")
    os.system("sudo ifconfig wlan0 down")
    mac=input("Enter the fake mac adress: ")
    os.system(f"sudo ifconfig wlan0 hw ether {mac}")
    os.system("sudo ifconfig wlan0 up")

def network_info():
    
    print("The network details are: \n\n")
    os.system("ifconfig")
network_info()
mac_spoof()
    
