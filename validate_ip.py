import sys


def validateIp(s):
    temp = s.split('.')
    if len(temp) !=4:
        return False

    for x in temp:
        if not x.isdigit():
            return False
        i = int(x)
        if i < 0 or i > 255:
            return False

    return True


def check():
    ip = raw_input("Enter Ipv4 Adresss: ")
    if validateIp(ip):
        print "Ip adress is Valid : %s"%ip
    else:
        print "Ip address is not valid"


check()
