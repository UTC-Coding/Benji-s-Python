# typo error in import
import subprocess

ping = 29
noice = 0

while noice==0:
    address = "169.254.246." + str(ping)
    res = subprocess.call(['ping', '-c', '1', address])
    ping += 1
    if res == 0:
        print "ping to", address, "OK"
        noice = 1
    elif res == 2:
        print "no response from", address
    else:
        print "ping to", address, "failed!"