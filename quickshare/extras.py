import os
from django.conf import settings

def system_info(info):
    try:
        ar = [x for x in info.split(';')]
        os = ar[1][1:]
        device = ar[2][1:]
        device = [x for x in device.split(')')]
    except: 
        return 'Unknown','Unknown'
    return os,device[0]


def get_attachments(card):
    names = []
    file_path = os.path.join(settings.MEDIA_ROOT,str(card.atmnt0))
    if os.path.exists(file_path):
        names.append(card.atmnt0.name)
    else:
        return names
    file_path = os.path.join(settings.MEDIA_ROOT,str(card.atmnt1))
    if os.path.exists(file_path):
        names.append(card.atmnt1.name)
    else:
        return names
    file_path = os.path.join(settings.MEDIA_ROOT,str(card.atmnt2))
    if os.path.exists(file_path):
        names.append(card.atmnt2.name)
    else:
        return names
    file_path = os.path.join(settings.MEDIA_ROOT,str(card.atmnt3))
    if os.path.exists(file_path):
        names.append(card.atmnt3.name)
    else:
        return names
    file_path = os.path.join(settings.MEDIA_ROOT,str(card.atmnt4))
    if os.path.exists(file_path):
        names.append(card.atmnt4.name)
    else:
        return names
    file_path = os.path.join(settings.MEDIA_ROOT,str(card.atmnt5))
    if os.path.exists(file_path):
        names.append(card.atmnt5.name)
    else:
        return names
    file_path = os.path.join(settings.MEDIA_ROOT,str(card.atmnt6))
    if os.path.exists(file_path):
        names.append(card.atmnt6.name)
    else:
        return names
    file_path = os.path.join(settings.MEDIA_ROOT,str(card.atmnt7))
    if os.path.exists(file_path):
        names.append(card.atmnt7.name)
    else:
        return names
    file_path = os.path.join(settings.MEDIA_ROOT,str(card.atmnt8))
    if os.path.exists(file_path):
        names.append(card.atmnt8.name)
    else:
        return names
    file_path = os.path.join(settings.MEDIA_ROOT,str(card.atmnt9))
    if os.path.exists(file_path):
        names.append(card.atmnt9.name)
    final=[]
    for x in names:
        if x != '' and x != None:
            x = x[6:]
            final.append(x)
    return final

        