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


