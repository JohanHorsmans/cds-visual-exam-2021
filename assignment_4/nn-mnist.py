#!/usr/bin/env python

# Loading packages:

# Import system tools:
import os
import sys
sys.path.append(os.path.join(".."))

# Import teaching utils to create a neural network:
from utils.neuralnetwork import NeuralNetwork

# Import sklearn metrics and functions:
from sklearn.preprocessing import LabelBinarizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn import datasets
from sklearn.datasets import fetch_openml
from sklearn.preprocessing import MinMaxScaler

# Import argparse to specify arguments in the script from the commandline.
import argparse

# Import numpy for working with arrays:
import numpy as np

# Import pickle to save neural network:
import pickle

# Import cv2 for working with images:
import cv2

# Import pandas for creating dataframes:
import pandas as pd

# Specify function called "str2bool" that allows one to specify boolean "False"- and "True" operators from the command-line in a plethora of different ways:
def str2bool(v):
    if isinstance(v, bool):
       return v
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')


# Define function argument defaults and how to specify them from the terminal:
ap = argparse.ArgumentParser(description = "[DESCRIPTION]: A function to classify images of numbers (from 0 - 9) with a neural network classifier. The following parameters can be specified, but you can also run the code with default parameters:")

ap.add_argument("-f", "--filename", default = "metrics_nn", type = str, help = "string, name of the file with evaluation metrics produced by the script. [DEFAULT]: metrics_nn")

ap.add_argument("-l", "--layers", default = [8, 16], nargs="*",  # nargs specifies that it should convert the input to a list.
type = int, help = "integer, specify amount of layers and their size (between the input and output layers): [DEFAULT]: 8 16")

ap.add_argument("-s", "--save", type=str2bool, nargs='?', const=True, default=True, help = "boolean, whether or not the fitted neural network model should be saved [DEFAULT]: True")

ap.add_argument("-c", "--custom", default = 0, type = str, help = "string, the path to a custom image that you would like to classify. [DEFAULT]: 0")

ap.add_argument("-e", "--epoch", default = 50, type = int, help = "integer, the amount of epochs you wish to run when fitting the model [DEFAULT]: 50")

# Parse the arguments
args = vars(ap.parse_args())

# Define the main function of the script and what parameters it takes: 
def main(filename, layers, save, custom, epoch):
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
                                                        test_size=2000) # Specify that the testing set should contain 2500 images.
    
    # Scale the image pixels from a range of [0:255] to [0:1].
    # The point of this is to even out the influence of pixel intensity range, since we are more interested in contour rather than contrast:
    X_train_scaled = X_train/255.0
    X_test_scaled = X_test/255.0
    
    # Binarize the classes to make it compatible with neural network structure (i.e. convert individual numbers, e.g. [1,2], to a binary representation, [[1,0],[0,1]]):    
    y_train = LabelBinarizer().fit_transform(y_train) 
    y_test = LabelBinarizer().fit_transform(y_test)
    
    # Adding the specified layers to the neural network structure:
    layers.insert(0, X_train.shape[1]) # Insert the number of pixels in the images as the amount of neurons in the input layer. 0 specifies that it should be added as the 0th element in the list.    
    layers.append(10) #  Insert the number of classes as the final output layer.
    
    # Define the network as "nn":
    nn = NeuralNetwork(layers)
    print("[INFO]: structure of the network: {}".format(nn)) #Sanity check for the user.
    
    print("[INFO]: Fitting neural network")
    # Fit the network to the training data with the specified amount of epochs:
    nn.fit(X_train_scaled, y_train, epochs=epoch)
    
    print("[INFO]: Predicting test data")
    # Predict the classes of the testing data and save it in an object calld "predictions":
    predictions = nn.predict(X_test_scaled)
    
    # Convert the predictions from individual probabilities for each class to a single binary prediction for the most probable class:
    predictions = predictions.argmax(axis=1)
    
    # Create a classification matrix with various metrics and save it as "cm":
    cm = classification_report(y_test.argmax(axis=1), predictions)
    
    # Print the classification matrix in the terminal:
    print(cm)
    
    # Specify that if there does not exist a folder called "out", in the directory of the script, it is to be made:
    if not os.path.exists("out"):
            os.makedirs("out")
    
    # Write the classification matrix to a .txt-file:
    doc = open(f"out/{filename}.txt", "w") # Create a document in the "out"-folder titled {filename}.txt
    doc.write(f"{cm}") # Write the classification matrix to the document.
    doc.close() # Close the document for further editing.
    
    print(f"[INFO]: The classification matrix has successfully been saved as \"{filename}.txt\" in the \"out\"-folder")
    
    if save == True:
        # Saving model
        outpath_nn_model = os.path.join("out", "nn.pkl")
        #joblib.dump(nn, outpath_nn_model)
        pickle.dump(nn, open(outpath_nn_model, 'wb'))
        #nn.save(outpath_nn_model)
        print(f"[INFO]: The trained neural network model has been saved as \"{outpath_nn_model}\" in the \"out\"-folder")
    
    # If the specified 'custom' argument is something other than default (i.e. 0), then do the following:
    if custom != 0:
        
        # Use cv2 to read the custom image:
        image = cv2.imread(custom)
        
        # Use cv2 to convert the custom image to grayscale:
        gray = cv2.bitwise_not(cv2.cvtColor(image, cv2.COLOR_BGR2GRAY))
        
        # Compress the image to the same size as the images in the mnist dataset, which the model has been trained on:
        compressed = cv2.resize(gray, (28, 28), interpolation=cv2.INTER_AREA)
        
        # Flatten the compressed image
        compressed_flattened = [float(item) for sublist in compressed for item in sublist] 
        
        # Converting the flattened compressed image to array
        compressed_flattened = np.array(compressed_flattened)
        
        # Scale the pixel-size of the custom image to be the same as the mnist dataset.
        scaler = MinMaxScaler()
        scaler = scaler.fit(X_train)
        compressed_flattened = pd.DataFrame(scaler.transform([compressed_flattened]))
        
        # # Predict the class of the custom image with the previously fitted model:
        custom_pred = nn.predict(compressed_flattened)
        
        # Save the most probable class as a binary prediction:
        custom_pred = int(custom_pred.argmax(axis=1))
        
        # Print the prediction in the terminal:
        print(f"[CLASSIFICATION]: I classify that the number depicted in \"{custom}\" is {custom_pred}") 

# Specify what to do when the script is called from the terminal, which is to run the "main()" function with the specified parameters:
if __name__ =="__main__":
    main(
    args["filename"],
    args["layers"],
    args["save"],
    args["custom"],
    args["epoch"])