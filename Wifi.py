import os
import xml.etree.ElementTree as ET
from selenium import webdriver
import time

name = input("Please Enter the Network Name: ")
password = input("Please Enter the Network Password: ")

mytree = ET.parse("Wifi-Sample.xml")
myroot = mytree.getroot()

myroot[0].text = str(name)
myroot[1][0][1].text = str(name)
myroot[4][0][1][2].text = str(password)
mytree.write("New_Wifi.xml")

os.system('netsh wlan add profile filename="New_Wifi.xml" interface="Wi-Fi"')
os.system('netsh wlan connect name="{}"'.format(name))

time.sleep(5)
driver = webdriver.Chrome()
driver.get("https://www.youtube.com/")



