import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Cria scatter plot
    fig, ax = plt.subplots(figsize=(20, 8))
    ax.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Cria a primeira melhor linha
    result = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])

    years_extended = pd.Series(range(1880, 2051))

    best_line = result.slope * years_extended + result.intercept

    ax.plot(years_extended, best_line, 'r')

    # Cria segunda melhor linha (a partir do ano 2000)
    df_new = df.loc[df['Year'] >= 2000]

    result_two = linregress(df_new['Year'], df_new['CSIRO Adjusted Sea Level'])

    years_extended_new = pd.Series(range(2000, 2051))

    best_line_two = result_two.slope * years_extended_new + result_two.intercept

    ax.plot(years_extended_new, best_line_two, 'g')

    # Adiciona as labels e título
    ax.set_title('Rise in Sea Level')
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()