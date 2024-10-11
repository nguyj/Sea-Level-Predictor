import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    fig, ax = plt.subplots(figsize=(8, 5))
    plt.scatter(df["Year"], df["CSIRO Adjusted Sea Level"])

    # Create first line of best fit
    lr_1880 = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
    plt.plot(range(1880, 2051, 1), lr_1880.slope * range(1880, 2051, 1) + lr_1880.intercept, "red")

    # Create second line of best fit
    lr_2000 = linregress(df[df["Year"] >= 2000]["Year"], df[df["Year"] >= 2000]["CSIRO Adjusted Sea Level"])
    plt.plot(range(2000, 2051, 1), lr_2000.slope * range(2000, 2051, 1) + lr_2000.intercept, "orange")

    # Add labels and title
    ax.set_title("Rise in Sea Level")
    ax.set_xlabel("Year")
    ax.set_ylabel("Sea Level (inches)")
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()