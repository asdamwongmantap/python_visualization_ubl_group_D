# TODO: All the code to produce your graphs for Stage 1 goes here!
from operator import index
from pickle import TRUE
from utils import *
import random
import numpy as np
import pandas as pd

# import matplotlib - very important
import matplotlib.pyplot as plt

def ri_outcome_each_country():
    # Getting the RI Traffic Stops dataset (Pandas DataFrame):
    ri_traffic_stops = get_ri_stops_df()
    
     # get data under age and each country
    subset_rtsProvidence = ri_traffic_stops[ri_traffic_stops["county_name"] == "Providence"]
    rtsPerCountryProvidenceStopOutCome = subset_rtsProvidence["stop_outcome"].value_counts().sort_index(ascending=True)

    subset_rtsKent = ri_traffic_stops[ri_traffic_stops["county_name"] == "Kent"]
    rtsPerCountryKentStopOutCome = subset_rtsKent["stop_outcome"].value_counts().sort_index(ascending=True)

    subset_rtsWashington = ri_traffic_stops[ri_traffic_stops["county_name"] == "Washington"]
    rtsPerCountryWashingtonStopOutCome = subset_rtsWashington["stop_outcome"].value_counts().sort_index(ascending=True)

    subset_rtsNewport = ri_traffic_stops[ri_traffic_stops["county_name"] == "Newport"]
    rtsPerCountryNewportStopOutCome = subset_rtsNewport["stop_outcome"].value_counts().sort_index(ascending=True)

    subset_rtsBristol = ri_traffic_stops[ri_traffic_stops["county_name"] == "Bristol"]
    rtsPerCountryBristolStopOutCome = subset_rtsBristol["stop_outcome"].value_counts().sort_index(ascending=True)

    # print(rtsPerCountryKentViolation)
    # get values
    line_one_ys = [i[1] for i in rtsPerCountryProvidenceStopOutCome.iteritems()]
    line_two_ys = [i[1] for i in rtsPerCountryKentStopOutCome.iteritems()]
    line_three_ys = [i[1] for i in rtsPerCountryWashingtonStopOutCome.iteritems()]
    line_four_ys = [i[1] for i in rtsPerCountryNewportStopOutCome.iteritems()]
    line_five_ys = [i[1] for i in rtsPerCountryBristolStopOutCome.iteritems()]
    Xs = [f'{i[0]}' for i in rtsPerCountryProvidenceStopOutCome.iteritems()]
    Xs.sort()

    # alright. construct our Figure and Axes (refer to lab)
    fig, ax = plt.subplots()
    
    ax.plot(Xs, line_one_ys, "red")
    ax.plot(Xs, line_two_ys, "green")
    ax.plot(Xs, line_three_ys, "blue")
    ax.plot(Xs, line_four_ys, "orange")
    ax.plot(Xs, line_five_ys, "yellow")

    # setting labels
    ax.set_xlabel("Stop OutCome")
    ax.set_ylabel("OutCome Total")
    ax.set_title("Outcome of traffic violations that occur")

    plt.show()

def ri_traffic_violations_year_each_country():
     # Getting the RI Traffic Stops dataset (Pandas DataFrame):
    ri_traffic_stops = get_ri_stops_df()
    
    # get data each year and each country
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

    # get values
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

def ri_offender_under_age():
    # Getting the RI Traffic Stops dataset (Pandas DataFrame):
    ri_traffic_stops = get_ri_stops_df()
    
     # get data under age and each country
    subset_rtsProvidence = ri_traffic_stops[ri_traffic_stops["county_name"] == "Providence"]
    subset_rtsProvidenceAge = subset_rtsProvidence[(subset_rtsProvidence["driver_age"] >= 16.00) & (subset_rtsProvidence["driver_age"] < 19.00)]
    rtsPerCountryProvidenceAge = subset_rtsProvidenceAge["driver_age"].value_counts().sort_index(ascending=True)

    subset_rtsKent = ri_traffic_stops[ri_traffic_stops["county_name"] == "Kent"]
    subset_rtsKentAge = subset_rtsKent[(subset_rtsKent["driver_age"] >= 16.00) & (subset_rtsKent["driver_age"] < 19.00)]
    rtsPerCountryKentAge = subset_rtsKentAge["driver_age"].value_counts().sort_index(ascending=True)

    subset_rtsWashington = ri_traffic_stops[ri_traffic_stops["county_name"] == "Washington"]
    subset_rtsWashingtonAge = subset_rtsWashington[(subset_rtsWashington["driver_age"] >= 16.00) & (subset_rtsWashington["driver_age"] < 19.00)]
    rtsPerCountryWashingtonAge = subset_rtsWashingtonAge["driver_age"].value_counts().sort_index(ascending=True)

    subset_rtsNewport = ri_traffic_stops[ri_traffic_stops["county_name"] == "Newport"]
    subset_rtsNewportAge = subset_rtsNewport[(subset_rtsNewport["driver_age"] >= 16.00) & (subset_rtsNewport["driver_age"] < 19.00)]
    rtsPerCountryNewportAge = subset_rtsNewportAge["driver_age"].value_counts().sort_index(ascending=True)

    subset_rtsBristol = ri_traffic_stops[ri_traffic_stops["county_name"] == "Bristol"]
    subset_rtsBristolAge = subset_rtsBristol[(subset_rtsBristol["driver_age"] >= 16.00) & (subset_rtsBristol["driver_age"] < 19.00)]
    rtsPerCountryBristolAge = subset_rtsBristolAge["driver_age"].value_counts().sort_index(ascending=True)

    # print(rtsPerCountryKentAge)
    # get values
    line_one_ys = [i[1] for i in rtsPerCountryProvidenceAge.iteritems()]
    line_two_ys = [i[1] for i in rtsPerCountryKentAge.iteritems()]
    line_three_ys = [i[1] for i in rtsPerCountryWashingtonAge.iteritems()]
    line_four_ys = [i[1] for i in rtsPerCountryNewportAge.iteritems()]
    line_five_ys = [i[1] for i in rtsPerCountryBristolAge.iteritems()]
    Xs = [f'{i[0]}' for i in rtsPerCountryProvidenceAge.iteritems()]
    Xs.sort()

    # alright. construct our Figure and Axes (refer to lab)
    fig, ax = plt.subplots()
    
    ax.plot(Xs, line_one_ys, "red")
    ax.plot(Xs, line_two_ys, "green")
    ax.plot(Xs, line_three_ys, "blue")
    ax.plot(Xs, line_four_ys, "orange")
    ax.plot(Xs, line_five_ys, "yellow")

    # setting labels
    ax.set_xlabel("Age")
    ax.set_ylabel("Offenders Total")
    ax.set_title("Offenders are under the age of 19")

    plt.show()

def ri_category_violations():
    # Getting the RI Traffic Stops dataset (Pandas DataFrame):
    ri_traffic_stops = get_ri_stops_df()
    
     # get data under age and each country
    subset_rtsProvidence = ri_traffic_stops[ri_traffic_stops["county_name"] == "Providence"]
    rtsPerCountryProvidenceViolation = subset_rtsProvidence["violation"].value_counts().sort_index(ascending=True)

    subset_rtsKent = ri_traffic_stops[ri_traffic_stops["county_name"] == "Kent"]
    rtsPerCountryKentViolation = subset_rtsKent["violation"].value_counts().sort_index(ascending=True)

    subset_rtsWashington = ri_traffic_stops[ri_traffic_stops["county_name"] == "Washington"]
    rtsPerCountryWashingtonViolation = subset_rtsWashington["violation"].value_counts().sort_index(ascending=True)

    subset_rtsNewport = ri_traffic_stops[ri_traffic_stops["county_name"] == "Newport"]
    rtsPerCountryNewportViolation = subset_rtsNewport["violation"].value_counts().sort_index(ascending=True)

    subset_rtsBristol = ri_traffic_stops[ri_traffic_stops["county_name"] == "Bristol"]
    rtsPerCountryBristolViolation = subset_rtsBristol["violation"].value_counts().sort_index(ascending=True)

    # print(rtsPerCountryKentViolation)
    # get values
    line_one_ys = [i[1] for i in rtsPerCountryProvidenceViolation.iteritems()]
    line_two_ys = [i[1] for i in rtsPerCountryKentViolation.iteritems()]
    line_three_ys = [i[1] for i in rtsPerCountryWashingtonViolation.iteritems()]
    line_four_ys = [i[1] for i in rtsPerCountryNewportViolation.iteritems()]
    line_five_ys = [i[1] for i in rtsPerCountryBristolViolation.iteritems()]
    Xs = [f'{i[0]}' for i in rtsPerCountryProvidenceViolation.iteritems()]
    Xs.sort()

    # alright. construct our Figure and Axes (refer to lab)
    fig, ax = plt.subplots()
    
    ax.plot(Xs, line_one_ys, "red")
    ax.plot(Xs, line_two_ys, "green")
    ax.plot(Xs, line_three_ys, "blue")
    ax.plot(Xs, line_four_ys, "orange")
    ax.plot(Xs, line_five_ys, "yellow")

    # setting labels
    ax.set_xlabel("Category Violation")
    ax.set_ylabel("Violation Total")
    ax.set_title("Categories of traffic violations that occur")

    plt.show()


if __name__ == "__main__":
    ri_outcome_each_country()
    ri_traffic_violations_year_each_country()
    ri_offender_under_age()
    ri_category_violations()
