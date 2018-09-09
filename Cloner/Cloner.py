print '\033[91m'
import os
import datetime
import urllib2
from BeautifulSoup import BeautifulSoup
import fcntl, socket, struct
from urllib2 import urlopen
from uuid import getnode as get_mac
mac = get_mac()
my_ip = urlopen('http://ip.42.pl/raw').read()
def getHwAddr(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    info = fcntl.ioctl(s.fileno(), 0x8927,  struct.pack('256s', ifname[:15]))
    return ':'.join(['%02x' % ord(char) for char in info[18:24]])
mymacadd = getHwAddr("eth0")
clear = lambda: os.system('clear')
clear()
day = datetime.datetime.today().weekday()
date = datetime.datetime.now()
newpath = r'Source'
if not os.path.exists(newpath):
    os.makedirs(newpath)
Credits = ("Made By Unsourced Team, 'Script Discontinued'\nCloned Website will,be located in Source 'Folder','Desktop/Cloner/Source'")
with open('Information.txt', 'w') as sd:
    for cred in Credits:
        sd.write(str(cred))
p1 = "  _   _                                        _ "
p2 = " | | | |                                      | |"
p3 = " | | | |_ __  ___  ___  _   _ _ __ ___ ___  __| |"
p4 = " | | | | '_ \/ __|/ _ \| | | | '__/ __/ _ \/ _` |"
p5 = " | |_| | | | \__ \ (_) | |_| | | | (_|  __/ (_| |"
p6 = "  \___/|_| |_|___/\___/ \__,_|_|  \___\___|\__,_|"
p7 = "                   Website Cloner"
logo = p1 + "\n" + p2 + "\n" + p3 + "\n" + p4+ "\n" + p5 + "\n" + p6 + "\n" + p7
print (logo)
print "\n\n"
print ("Your Ip : " + my_ip)
print ("Your Mac Address is : " + mymacadd + "\n\n")
webs = raw_input('Website: ')
soup = BeautifulSoup(urllib2.urlopen(webs).read())
with open('Source/source.txt', 'w') as f:
    for websitehtml in soup:
        f.write(str(websitehtml))
with open('Source/Website Cloned.html', 'w') as sd:
    for websitehtml2 in soup:
        sd.write(str(websitehtml2))
clear()
print (logo)
print "\n\nFile Located in Source 'Folder' , 'Desktop/Cloner/Source'"