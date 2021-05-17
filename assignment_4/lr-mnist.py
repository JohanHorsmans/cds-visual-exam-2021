#!/usr/bin/env python

# Loading packages:

# Import system tools:
import os
import sys
sys.path.append(os.path.join(".."))

# Import teaching utils (modified by me to solve this assignment):
import utils.classifier_utils as clf_util

# Import sklearn metrics and functions:
from sklearn import metrics
from sklearn.datasets import fetch_openml
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Import numpy for working with arrays:
import numpy as np

# Import pandas for creating dataframes:
import pandas as pd

# Import cv2 for working with images:
import cv2

# Import argparse to specify arguments in the script from the commandline.
import argparse

#TEST 
def str2bool(v):
    if isinstance(v, bool):
       return v
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')
##


# Define function argument defaults and how to specify them from the terminal:
ap = argparse.ArgumentParser(description = "[DESCRIPTION]: A function to classify images of numbers (from 0 - 9) with a logistic regression model. The following parameters can be specified, but you can also run the code with default parameters:")

ap.add_argument("-f", "--filename", default = "metrics_lr", type = str, help = "string, name of the file with evaluation metrics produced by the script. [DEFAULT]: metrics_lr")

ap.add_argument("-c", "--custom", default = 0, type = str, help = "string, the path to a custom image that you would like to classify. [DEFAULT]: 0")

ap.add_argument("-t", "--tolerance", default = 0.1, type = float, help = "float, tolerance for stopping criteria for logistic regression model. [DEFAULT]: 0.1")

ap.add_argument("-p", "--penalty", default = 'none', type = str, help = "str, penalization type for logistic regresion model. (for options see: https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html). [DEFAULT]: none")

# Parse the arguments
args = vars(ap.parse_args())

# Define the main function of the script and what parameters it takes: 
def main(filename, custom, penalty, tolerance):
    print("[INFO]: Loading mnist-data")
    # Loading the mnist dataset:
    X, y = fetch_openml('mnist_784', version=1, return_X_y=True) # X = pixel values, y = class (i.e. number depicted).
    
    print("[INFO]: Preprocessing data")
    # Convert to numpy array:
    X = np.array(X)
    y = np.array(y)
    
    # Split the data into a train- and test set:
    X_train, X_test, y_train, y_test = train_test_split(X, 
                                                        y, 
                                                        random_state=9, # Making the split replicable.
                                                        train_size=20000, # Specify that the training set should contain 20000 images.
                                                        test_size=2500) # Specify that the testing set should contain 2500 images.
    
    # Scale the image pixels from a range of [0:255] to [0:1].
    # The point of this is to even out the influence of pixel intensity range, since we are more interested in contour rather than contrast:
    X_train_scaled = X_train/255.0
    X_test_scaled = X_test/255.0
    
    print("[INFO]: Fitting logistic regression model")
    # Fit a logistic regression model to the training data:
    clf = LogisticRegression(penalty = penalty, # Penalty-type (specified from command-line).
                            tol = tolerance, # Tolerance for stopping criteria for the model.
                            solver = 'saga', # Specify optimization algortihm.
                            multi_class = 'multinomial').fit(X_train_scaled, y_train) # Specify that the data ha multiple classes.
    
    print("[INFO]: Predicting test data")
    # Predict the classes in the test data, with fhe fitted model and save them in an object called "y_pred":
    y_pred = clf.predict(X_test_scaled)
    
    # Create a classification matrix with various metrics and save it as "cm":
    cm = metrics.classification_report(y_test, y_pred)
    
    # Print the classification matrix in the terminal:
    print(cm)
    
    # Specify that if there does not exist a folder called "out", in the directory of the script, it is to be made:
    if not os.path.exists("out"):
            os.makedirs("out")
    
    # Write the classification matrix to a .txt-file:
    doc = open(f"out/{filename}.txt", "w") # Create a document in the "out"-folder titled {filename}.txt
    doc.write(f"{cm}") # Write the classification matrix to the document.
    doc.close() # Close the document for further editing.
    
    print(f"[INFO]: The classification matrix has successfully been saved as {filename}.txt")
    
    # Specify custom image argument:
    
    # If the specified 'custom' argument is something other than default (i.e. 0), then do the following:
    if custom != 0: 
                
        # Define possible classes (i.e. 0 -> 9):
        classes = sorted(set(y))
        
        # Use cv2 to read the custom image:
        image = cv2.imread(custom) 
        
        # Use cv2 to convert the custom image to grayscale:
        gray = cv2.bitwise_not(cv2.cvtColor(image, cv2.COLOR_BGR2GRAY))
        
        # Compress the image to the same size as the images in the mnist dataset, which the model has been trained on:
        compressed = cv2.resize(gray, (28, 28), interpolation=cv2.INTER_AREA)
        
        # Predict the class of the custom image with the previously fitted model:
        custom_pred = clf_util.predict_unseen_ass_4(compressed, clf, classes) # Using a modified version of the "predict_unseen"-function found in the "utils"-script. The modification removes the "print" argument specified in the original function.
        
        # Print the prediction in the terminal:
        print(f"[CLASSIFICATION]: I classify that the number depicted in \"{custom}\" is: {custom_pred}")

# Specify what to do when the script is called from the terminal, which is to run the "main()" function with the specified parameters:
if __name__ =="__main__":
    main(
    args["filename"],
    args["custom"],
    args["penalty"],
    args["tolerance"])