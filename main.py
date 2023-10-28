import pandas as pd
import matplotlib.pyplot as plt

def read_file(file_name):
    # create the data summary
    df = pd.read_csv(file_name)
    return df

def summary(file_name):
    df=read_file(file_name)
    return df.describe()

def summary_plot(file_name):
    df=read_file(file_name)

    plt.hist(df['IMDB_Rating'])
    plt.show()



