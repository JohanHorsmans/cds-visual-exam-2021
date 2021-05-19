<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/JohanHorsmans/cds-visual-exam-2021">
    <img src="../README_images/computer vision.png" alt="Logo" width="142" height="131">
  </a>
  
  <h1 align="center">Cultural Data Science 2021</h1> 
  <h3 align="center">Assignment 4</h3> 

  <p align="center">
    Johan Kresten Horsmans
    <br />
    <a href="https://github.com/JohanHorsmans/cds-visual-exam-2021.pdf"><strong>Link to portfolio descriptions »</strong></a>
    <br />
  </p>
</p>

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#offical-description-from-instructor">Offical description from instructor</a></li>
    <li><a href="#methods">Methods</a></li>
    <li><a href="#how-to-run">How to run</a></li>
    <li><a href="#repository-structure-and-contents">Repository structure and contents</a></li>
  </ol>
</details>

<!-- OFFICIAL DESCRIPTION FROM INSTRUCTOR -->
## Offical description from instructor

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

<!-- METHODS -->
## Methods

This problem of this assignment relates to using predictive models to classify greyscale images of hand drawn numbers in the MNIST dataset and evaluating the model classifications. For the logistic regression classifier, I used the LogisticRegression-function from sklearn.linear_model. For the neural network, I created a dense network where you could specify the structure and size of the layers between the input and the output as an argument called --layers. The default structure of the neural network is [224, 8, 16, 10]. Note that my script uses the same data for validation and testing. Furthermore, I solved all of the bonus assignments. For the tasks that required specifying arguments from the terminal, I used argparse. 
For model evaluation, I have chosen to use macro F1-score as my metric: 

The F1-score is a metric devised to fuse the relation between model precision and recall into a unified score. The metric is defined as taking the harmonic mean of precision and recall. The reason for using the harmonic mean, rather than the arithmetic mean, is that the harmonic mean of a recall-score of 0 and a precision-score of 100 would result in an F1-score of 0, rather than 50. This is advantageous, since it means that a model cannot achieve a high F1-score by having a high recall or precision by itself. The macro-averaging procedure of the macro F1-score involves calculating the arithmetic mean of the F1-score for each class.

<!-- HOW TO RUN -->
## How to run

__NOTICE:__ To run the assignment, you need to have configured and activated your virtual environment. See the main [README](https://github.com/JohanHorsmans/cds-visual-exam-2021/blob/main/README.md) for a guide on how to do this.

Go through the following steps to run assignment 4:
```bash
cd {root directory (i.e. cds-visual-exam-2021}
cd assignment_4
python3 lr-mnist.py
python3 nn-mnist.py
```
Type: ```python3 lr-mnist.py -h``` and ```python3 nn-mnist.py -h``` for a detailed guide on how to specify script-parameters. 

<!-- REPOSITORY STRUCTURE AND CONTENTS -->
## Repository structure and contents

This repository contains the following files:
|File|Description|
|:--------|:-----------|
```lr-mnist.py``` | The python script for the logistic regression assignment
```nn-mnist.py``` | The python script for the neural network assignment
```README.md``` | The README file that you are currently reading.

<!-- DISCUSSION OF RESULTS -->
## Discussion of results

For the neural network model, I achieved a macro F1-score of 0.89 after training for 50 epochs. For the logistic regression model, I achieved a macro F1-score of 0.91 using a tolerance of 0.1 and no penalty. When testing the models with custom image-files the performance dropped drastically indicating that the models are overfitting to the specifics of the MNIST-dataset, leading to low generalizability. 

<br />
<p align="center">
  <a href="https://github.com/JohanHorsmans/cds-visual-exam-2021">
    <img src="../README_images/logo_au.png" alt="Logo" width="300" height="102">
  </a>
