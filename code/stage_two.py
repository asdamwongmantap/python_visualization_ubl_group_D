# TODO: All the code to produce your graphs for Stage 2 goes here!
from operator import index
from pickle import TRUE
from utils import *
import random
import numpy as np
import pandas as pd

# import matplotlib - very important
import matplotlib.pyplot as plt

def ri_predict_is_arrested():
    dataset_name = "ri_traffic_stops"
    model_name = "decision_tree"
    target_name = "is_arrested"
    feature_names = ["driver_gender", "driver_age", "stop_duration"]
    training_acc,testing_acc = customized_ml_model_call_with_param(dataset_name,model_name,target_name,feature_names)
    print(f"\n\n----- Accuracy For Model {model_name} Trained On Dataset {dataset_name} To Predict Is Arrested-----\n\n")
    print(f"Features: {feature_names}")
    print(f"Training accuracy: {training_acc}")
    print(f"Testing accuracy: {testing_acc}")

def ri_predict_traffic_violation():
    dataset_name = "ri_traffic_stops"
    model_name = "decision_tree"
    target_name = "search_conducted"
    feature_names = ["violation", "driver_race", "drugs_related_stop"]
    training_acc,testing_acc = customized_ml_model_call_with_param(dataset_name,model_name,target_name,feature_names)
    print(f"\n\n----- Accuracy For Model {model_name} Trained On Dataset {dataset_name} To Predict Traffic Violation-----\n\n")
    print(f"Features: {feature_names}")
    print(f"Training accuracy: {training_acc}")
    print(f"Testing accuracy: {testing_acc}")

def ri_predict_stop_duration():
    dataset_name = "ri_traffic_stops"
    model_name = "decision_tree"
    target_name = "stop_duration"
    feature_names = ["violation", "driver_age"]
    training_acc,testing_acc = customized_ml_model_call_with_param(dataset_name,model_name,target_name,feature_names)
    print(f"\n\n----- Accuracy For Model {model_name} Trained On Dataset {dataset_name} To Predict Impact Stop Duration-----\n\n")
    print(f"Features: {feature_names}")
    print(f"Training accuracy: {training_acc}")
    print(f"Testing accuracy: {testing_acc}")


if __name__ == "__main__":
    ri_predict_is_arrested()
    ri_predict_traffic_violation()
    ri_predict_stop_duration()
