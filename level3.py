def two_laptops(ssd, hdd):
    # Determining if prices are even numbers
    if ssd % 2 == 0 and hdd % 2 == 0:
        return min(ssd,hdd)
    else:
        return max(ssd,hdd)
# Calling the function with even or odd combination.Run with one at a time.
two_laptops(300000, 250000)
two_laptops(300000, 250005)            