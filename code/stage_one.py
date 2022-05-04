# TODO: All the code to produce your graphs for Stage 1 goes here!
from operator import index
from utils import *
import random
import numpy as np
import pandas as pd

# import matplotlib - very important
import matplotlib.pyplot as plt

def ri_traffic_violations_each_country():
     # Getting the RI Traffic Stops dataset (Pandas DataFrame):
    ri_traffic_stops = get_ri_stops_df()
    
     # get data each year
    subset_rtsProvidence = ri_traffic_stops[ri_traffic_stops["county_name"] == "Providence"]
    rtsPerCountryProvidence = subset_rtsProvidence["stop_year"].value_counts()
    subset_rtsKent = ri_traffic_stops[ri_traffic_stops["county_name"] == "Kent"]
    rtsPerCountryKent = subset_rtsKent["stop_year"].value_counts()
    subset_rtsWashington = ri_traffic_stops[ri_traffic_stops["county_name"] == "Washington"]
    rtsPerCountryWashington = subset_rtsWashington["stop_year"].value_counts()
    subset_rtsNewport = ri_traffic_stops[ri_traffic_stops["county_name"] == "Newport"]
    rtsPerCountryNewport = subset_rtsNewport["stop_year"].value_counts()
    subset_rtsBristol = ri_traffic_stops[ri_traffic_stops["county_name"] == "Bristol"]
    rtsPerCountryBristol = subset_rtsBristol["stop_year"].value_counts()
    # just constructing some dummy data
    line_one_ys = [i[1] for i in rtsPerCountryProvidence.iteritems()]
    line_two_ys = [i[1] for i in rtsPerCountryKent.iteritems()]
    line_three_ys = [i[1] for i in rtsPerCountryWashington.iteritems()]
    line_four_ys = [i[1] for i in rtsPerCountryNewport.iteritems()]
    line_five_ys = [i[1] for i in rtsPerCountryBristol.iteritems()]
    Xs = [i[0] for i in rtsPerCountryProvidence.iteritems()]
    # alright. construct our Figure and Axes (refer to lab)
    fig, ax = plt.subplots()
    
    ax.plot(Xs, line_one_ys, "red")
    ax.plot(Xs, line_two_ys, "green")
    ax.plot(Xs, line_three_ys, "blue")
    ax.plot(Xs, line_four_ys, "orange")
    ax.plot(Xs, line_five_ys, "yellow")

    # setting labels
    ax.set_xlabel("Year")
    ax.set_ylabel("Violations Total")
    ax.set_title("Traffic Violations Each country")

    plt.show()


if __name__ == "__main__":
    ri_traffic_violations_each_country()
