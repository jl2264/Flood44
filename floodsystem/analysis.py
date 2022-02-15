import numpy as np
import matplotlib.pyplot as plt
import matplotlib

def polyfit(dates, levels, p):
    
    x = matplotlib.dates.date2num(dates)
    y = levels
    
    p_coeff = np.polyfit(x-x[0], y, p)

    poly = np.poly1d(p_coeff)
    
    return poly, x[0]
  


