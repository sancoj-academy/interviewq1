def two_laptops(ssd, hdd):
    # Determining if prices are even numbers
    if ssd % 2 == 0 and hdd % 2 == 0:
        # Checking the lesser price
        if ssd > hdd:
            return hdd
        else:
            return sdd
    # Confirming if prices are odd numbers        
    elif ssd % 2 == 1 or hdd % 2 == 1:
        # Checking the higher price
        if ssd > hdd:
            return ssd
        else:
            return hdd 
    # Determining if sum of prices is odd number
    elif (ssd + hdd) % 2 == 1:
        if ssd > hdd:
            return ssd
        else:
            return hdd  
# Calling the function with even and/or odd combination
two_laptops(300000, 250000)
two_laptops(300000, 250005)                                
