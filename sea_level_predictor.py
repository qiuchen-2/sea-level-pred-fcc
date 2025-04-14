import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']
    fig, ax =plt.subplots()

    # Create first line of best fit
    res= linregress(x,y)
    x0 = pd.Series([i for i in range(1880, 2051)])
    y0 = res.slope*x0 + res.intercept

    plt.plot(x, y, 'o', alpha =0.5)
    plt.plot(x0, y0, 'r')

    
    # Create second line of best fit
    new_df_2050 = df.loc[df['Year'] >= 2000]
    new_x = new_df_2050['Year']
    new_y = new_df_2050['CSIRO Adjusted Sea Level']

    res1= linregress(new_x,new_y)

    x1 = pd.Series([i for i in range(2000, 2051)])
    y1 = res1.slope*x1 + res1.intercept

    plt.plot(x1, y1, 'y')


    # Add labels and title
    plt.title('Rise in Sea Level')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.legend()
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()