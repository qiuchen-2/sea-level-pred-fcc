import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']

    # Create first line of best fit
    res= linregress(x,y) #Linear Regression
    x0 = pd.Series(range(1880,2051)) #needs to go to 2051 since index starts at 0, and if 2050 it ends at 2049
    y0 = res.slope*x0 + res.intercept #Line of best fit

    plt.scatter(x, y, alpha =0.5)
    plt.plot(x0, y0, 'r')

    
    # Create second line of best fit
    df_2000_2050 = df[df['Year'] >= 2000]
    x_2000_2050 = df_2000_2050['Year'] #x labels are still attributed to Year
    y_2000_2050 = df_2000_2050['CSIRO Adjusted Sea Level'] #y labels are still attributed to Sea Levels

    res_2000_2050 = linregress(x_2000_2050, y_2000_2050)

    x1 = pd.Series(range(2000,2051)) #needs to go to 2051 since index starts at 0, and if 2050 it ends at 2049
    y1 = res_2000_2050.slope*x1 + res_2000_2050.intercept #From Scipy documentation

    plt.plot(x1, y1, 'r')


    # Add labels and title
    plt.title('Rise in Sea Level')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.legend()
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()