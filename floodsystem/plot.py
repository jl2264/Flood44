from threading import local
from turtle import color
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from .analysis import polyfit
import matplotlib


def plot_water_levels(station, dates, levels):
    #print(dates)
    plt.plot(dates, levels)

# Add axis labels, rotate date labels and add plot title
    plt.xlabel('dates')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45)
    plt.title(station.name)
    plt.axhline(station.typical_range[0], linestyle= '--', color = 'red')
    plt.axhline(station.typical_range[1], linestyle= '--', color = 'red')


# Display plot
    plt.tight_layout()  # This makes sure plot does not cut off date labels

    plt.show()

def plot_water_level_with_fit(station, dates, levels, p):
    
    levels_polyfit = polyfit(dates, levels, p)[0](matplotlib.dates.date2num(dates)-polyfit(dates, levels, p)[1])
    plt.plot(dates, levels_polyfit, color = 'orange')
    plt.plot(dates, levels, color = 'blue')
    plt.xlabel('dates')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45)
    plt.title(station.name)
    plt.axhline(station.typical_range[0], linestyle= '--', color = 'red')
    plt.axhline(station.typical_range[1], linestyle= '--', color = 'red')
    plt.tight_layout()

    plt.show()

def slope(x1, y1, x2, y2):
    m = (y2-y1)/(x2-x1)
    return m

def relative_level_rising_rate(station, dates, levels):
    dates1 = matplotlib.dates.date2num(dates)
    rates_of_change = []
    sum = 0
    for i in range(len(dates1)):
        local_rate_of_change = slope(dates1[i-1], levels[i-1], dates1[i], levels[i])
        sum += local_rate_of_change
        rates_of_change.append(local_rate_of_change)
    overall_rate = sum/len(dates1)
    return overall_rate
'''
    for i in range(-1, -20):
        sum += float(rates_of_change[i])
    overall_rate = sum/20
    return overall_rate

'''





