def two_laptops(ssd, hdd):
    # Determining if prices are even numbers
    if ssd % 2 == 0 and hdd % 2 == 0:
        if ssd > hdd:
            return hdd
        else:
            return ssd
    else:  
        if ssd > hdd:
            return ssd
        else:
            return hdd 
# Calling the function with even or odd combination.Run with one at a time.
two_laptops(300000, 250000)
two_laptops(300000, 250005) 