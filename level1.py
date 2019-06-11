def two_laptops(ssd, hdd):
    if ssd % 2 == 0 and hdd % 2 == 0:
        if ssd > hdd:
            return hdd
        else:
            return sdd
    elif ssd % 2 == 1 or hdd % 2 == 1:
        if ssd > hdd:
            return ssd
        else:
            return hdd                
