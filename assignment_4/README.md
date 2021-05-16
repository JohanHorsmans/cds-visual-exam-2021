# Assignment 4 - Classification benchmarks

## DESCRIPTION
__Classifier benchmarks using Logistic Regression and a Neural Network__

This assignment builds on the work we did in class and from session 6.

You'll use your new knowledge and skills to create two command-line tools which can be used to perform a simple classification task on the MNIST data and print the output to the terminal. These scripts can then be used to provide easy-to-understand benchmark scores for evaluating these models.

You should create two Python scripts. One takes the full MNIST data set, trains a Logistic Regression Classifier, and prints the evaluation metrics to the terminal. The other should take the full MNIST dataset, train a neural network classifier, and print the evaluation metrics to the terminal.

__Tips__
* I suggest using scikit-learn for the Logistic Regression Classifier
* In class, we only looked at a small sample of MNIST data. I suggest using fetch_openml() to get the full dataset, like we did in session 6
* You can use the NeuralNetwork() class that I introduced you to during the code along session
* I recommend saving your .py scripts in a folder called src﻿; and have your NeuralNetwork class in a folder called utils, like we have on worker02
* You may need to do some data manipulation to get the MNIST data into a usable format for your models
* If you have trouble doing this on your own machine, use worker02!


__Bonus Challenges__
* Have the scripts save the classifier reports in a folder called out, as well as printing them to screen. Add the user should be able to define the file name as a command line argument (easier)
* Allow users to define the number and size of the hidden layers using command line arguments (intermediate)
* Allow the user to define Logistic Regression parameters using command line arguments (intermediate)
* Add an additional step where you import some unseen image, process it, and use the trained model to predict it's value - like we did in session 6 (intermediate)
* Add a new method to the Neural Network class which will allow you to save your trained model for future use (advanced)

__General instructions__
* Save your script as lr-mnist.py and nn-mnist.py
* If you have external dependencies, you must include a requirements.txt
* You can either upload the script here or push to GitHub and include a link - or both!
* Your code should be clearly documented in a way that allows others to easily follow along
* Similarly, remember to use descriptive variable names! A name like X_train is (just) more readable than x1.
* The filenames of the saved images should clearly relate to the original image

__Purpose__ 
This assignment is designed to test that you have a understanding of:

* how to train classification models using machine learning and neural networks;
* how to create simple models that can be used as statistical benchmarks;
* how to do this using scripts which can be executed from the command line