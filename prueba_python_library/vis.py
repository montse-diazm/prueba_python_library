import matplotlib.pyplot as plt
import pandas as pd

def plot_viz_barchart_01(df, x_col, y_col):
    df.plot(kind='bar', x=x_col, y=y_col, legend=False)
    plt.xlabel(x_col)
    plt.ylabel(y_col)
    plt.title(f'Bar chart of {y_col} vs {x_col}')
    plt.show()