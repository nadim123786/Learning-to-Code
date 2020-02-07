import os
import unittest
os.system("ipconfig >d:\\test.txt")

filename = "D:\\test.txt"
with open(filename) as file_object:
    lines = file_object.readlines()
iplist = []
for line in lines:
    iplist.append(line)

a = (iplist.index("Wireless LAN adapter Wi-Fi:\n"))
b = (iplist.index("Wireless LAN adapter Local Area Connection* 2:\n"))

for value in iplist[a:b]:
    if "IPv4" in value:
        c = value.split(":")

ipadd = (c[1].lstrip())
ipaddress = ipadd.rstrip()

os.system("cls")
os.system("ping {} >d:\\ping.txt".format(ipaddress))

filename1 = "d:\\ping.txt"
with open(filename1) as file_object1:
    lines1 = file_object1.readlines()

for line in lines1:
    if "Packets:" in line:
        d = line.strip()
        e = d.split()


class TestPing(unittest.TestCase):
    def test_ping(self):
        self.assertTrue(e[3] == e[6])


if __name__ == "__main__":
    unittest.main()