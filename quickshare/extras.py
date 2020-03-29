from os import uname

def system_info(info):
    try:
        ar = [x for x in info.split(';')]
        os = ar[1][1:]
        device = ar[2][1:]
        device = [x for x in device.split(')')]
    except: 
        return 'Unknown','Unknown'
    return os,device[0]

