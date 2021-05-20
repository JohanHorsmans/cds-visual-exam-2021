#!/usr/bin/env python

# Loading packages:

# Import system tools:
import os
import sys
sys.path.append(os.path.join(".."))

# Import cv2 for working with images:
import cv2

# Import argparse to specify arguments in the script from the commandline:
import argparse

# Import numpy for working with arrays:
import numpy as np

# Import matplotlib for plots:
import matplotlib.pyplot as plt

# Import sklearn tools for metrics:
from sklearn.metrics import classification_report

# Import tensorflow and keras for machine learning:
import tensorflow as tf
import keras
from keras.models import Sequential
from keras.layers import Dense, Conv2D , MaxPool2D , Flatten , Dropout 
from keras.preprocessing.image import ImageDataGenerator
from keras.optimizers import SGD

# Suppress warnings:
import warnings
warnings.filterwarnings('ignore')

# Define function argument defaults and how to specify them from the terminal:
ap = argparse.ArgumentParser(description = "[DESCRIPTION]: A script to classify artists from paintings. The following parameters can be specified, but you can also run the code with default parameters:")

ap.add_argument("-e", "--epochs", default = "10", type = int, help = "string, name of the file with evaluation metrics produced by the script. [DEFAULT]: 10")

# Parse the arguments
args = vars(ap.parse_args())

# Define the main function of the script and what parameters it takes: 
def main(epochs):
    
# Define the data-classes in a list called "labels"
    labels = ['Cezanne', 'Degas', 'Gauguin', 'Hassam', 'Matisse', 'Monet', 'Pissarro', 'Renoir', 'Sargent', 'VanGogh']
    
# Define a function to load the data and convert it into a suitable format for the CNN classifiers:
    def get_data(directory): # Define function called "get_data" that takes "directory" as input variable:
        data = [] # Define empty list called "data".
        for label in labels: # For each label in the list "labels" ...
            path = os.path.join(directory, label)  # ... Specify the path as "directory/label" 
            class_num = labels.index(label) # ... Specify "class_num" as the index of the current label in the "labels"-list (i.e. Cezanne = 0 and Gauguin = 3)
            for img in os.listdir(path): # For each image in "path" ...
                img_arr = cv2.imread(os.path.join(path, img))[...,::-1] # Read the image, convert BGR to RGB-format and save it as a variable named "img_arr"
                resized_arr = cv2.resize(img_arr, (224, 224)) # ... Reshape the image to 224 x 224.
                data.append([resized_arr, class_num]) # Append the image to the "data"-list as the first element and the class as the second element. 
        return np.array(data) # When done, convert data to a numpy-array.
    
    # Use above function to load train- and test data:
    print("[INFO]: Loading training data")
    train = get_data("data/training/training") 
    
    print("[INFO]: Loading testing data")
    test = get_data("data/validation/validation")

    
    print("[INFO]: Preprocessing data")
    
    # Data preprocesing:

    # Define empty lists for data. The x's are for images and the y's are for classes. I'm using the same data for testing and validation.
    x_train = [] 
    y_train = []
    x_test = []
    y_test = []

    # Create training data:
    for array, label in train: # For each array (first element) and each label (second element) in train...
        x_train.append(array) # ... Append array to "x_train".
        y_train.append(label) # ... Append label to "y_train"

    for array, label in test: # For each array (first element) and each label (second element) in test...
        x_test.append(array) # ... Append array to "x_test".
        y_test.append(label) # ... Append label to "y_test"

    # Normalizing the pixel range for 0 -> 255 to 0 -> 1:
    x_train = np.array(x_train) / 255
    x_test = np.array(x_test) / 255

    # Converting labels to array-format:
    y_train = np.array(y_train)
    y_test = np.array(y_test)

    # Transform the labels to a one-hot tensor (to fit the pretrained model):
    y_train = tf.one_hot(y_train, depth=len(labels))
    y_test = tf.one_hot(y_test, depth=len(labels))
    
    print("[INFO]: loading pretrained model")
    # Load pretrained model (MobileNetV2) without the final classificaion layer:
    pretrained_model = tf.keras.applications.MobileNetV2(input_shape = (224, 224, 3), include_top = False, weights = "imagenet") #

    # Freeze model to prevent updating weights in pretrained base-model:
    pretrained_model.trainable = False
    
    # Initialize keras-model with some extra layers on top: 
    model = tf.keras.Sequential([pretrained_model, 
                                     tf.keras.layers.GlobalAveragePooling2D(), # Add an average pooling layer.
                                     tf.keras.layers.Dropout(0.6), # Add dropout layer, wih 40% of the layer inputs set to 0 (to avoid overfitting).
                                     tf.keras.layers.Dense(10, activation="softmax") # Add a dense layer with 10 output nodes (one for each class).                                     
                                    ])
    
    # Define adam optimizer with a high learning rate to increase training efficiency.
    optimizer = SGD(lr = 0.01) 

    # Compile model with CategoricalCrossentropy loss function and the above optimizer.
    model.compile(optimizer=optimizer,
                  loss=tf.keras.losses.CategoricalCrossentropy(from_logits=True),
                  metrics=['accuracy'])
    
    # Train the model for specified number of epochs:

    epochs = epochs # Define epochs-variable as argument specified in the terminal.

    print("[INFO]: Fitting model")
    fitted_model = model.fit(x_train,y_train,epochs = epochs, validation_data = (x_test, y_test))
    
    # Plot accuracy and loss as a function of epochs.

    acc = fitted_model.history['accuracy'] # Save accuracy history for training data as "acc"
    val_acc = fitted_model.history['val_accuracy'] # Save accuracy history for testing data as "val_acc"
    loss = fitted_model.history['loss'] # Save loss history for training data as "loss"
    val_loss = fitted_model.history['val_loss'] # Save loss history for testing data as "val_loss"

    epochs_range = range(epochs) # Define the range of the epochs.

    plt.figure(figsize=(15, 15)) # Initialize plot-surface.
    plt.subplot(2, 2, 1) # Initialize first subplot.
    plt.plot(epochs_range, acc, label='Training Accuracy') # Plot x = "epochs_range", y = "acc".
    plt.plot(epochs_range, val_acc, label='Validation Accuracy') # Plot x = "epochs_range", y = "val_acc".
    plt.legend(loc='lower right') # Add legend.
    plt.title('Training and Validation Accuracy') # Add title.

    plt.subplot(2, 2, 2) # Initialize second subplot. 
    plt.plot(epochs_range, loss, label='Training Loss') # Plot x = "epochs_range", y = "loss".
    plt.plot(epochs_range, val_loss, label='Validation Loss') # Plot x = "epochs_range", y = "val_loss".
    plt.legend(loc='upper right') # Add legend.
    plt.title('Training and Validation oss') # Add title.
    plt.savefig('val_acc.png') # Save the plot as "val_acc.png".
    print("[INFO]: Model training metrics has been successfully saved as \"val_acc.png\" in the \"assignment_5\"-folder")
    
    # Recreate testing labels to convert them back to their original format (from a one-hot tensor):
    y_test = []

    for feature, label in test:
        y_test.append(label)

    y_test = np.array(y_test)

    print("[INFO]: Predicting testing data")
    # Predict classes of test data:
    predictions = model.predict_classes(x_test)

    # Create classification report:
    cm = classification_report(y_test, predictions, target_names = ['Cezanne', 'Degas', 'Gauguin', 'Hassam', 'Matisse', 'Monet', 'Pissarro', 'Renoir', 'Sargent', 'VanGogh'])
    
    # Print classification report:
    print(cm) 
    
    # Write the classification matrix to a .txt-file called "cm.txt":
    doc = open("cm.txt", "w") # Create a document in the "out"-folder titled {filename}.txt
    doc.write(f"{cm}") # Write the classification matrix to the document.
    doc.close() # Close the document for further editing.
    print("[INFO]: The classification matrix has successfully been saved as cm.txt in the \"assignment_5\"-folder")


if __name__ =="__main__":
    main(
    args["epochs"])
