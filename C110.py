import csv 
import plotly.figure_factory as ff
import pandas as pd
import statistics
import random
import plotly.graph_objects as go

df = pd.read_csv("medium_data.csv")
population_mean = df["reading_time"].tolist()


def random_set_of_mean(counter):
    dataset = []
    for i in range(0,counter):
        random_index = random.randint(0,len(population_mean))
        value = population_mean[random_index]
        dataset.append(value)
   
    mean = statistics.mean(dataset)
    return mean

def setup():
    mean_list = []
    for i in range(0,100):
        set_of_means = random_set_of_mean(30)
        mean_list.append(set_of_means)
    
    show_fig(mean_list)
        

def show_fig(mean_list):
    df = mean_list
    fig = ff.create_distplot([df],["reading_time"],show_hist=False)
    fig.show()


setup()