<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/JohanHorsmans/cds-visual-exam-2021">
    <img src="../README_images/computer vision.png" alt="Logo" width="142" height="131">
  </a>
  
  <h1 align="center">Cultural Data Science 2021</h1> 
  <h3 align="center">Assignment 3</h3> 

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
    <li><a href="#official-description-from-instructor">Official description from instructor</a></li>
    <li><a href="#how-to-run">How to run</a></li>
    <li><a href="#repository-structure-and-contents">Repository structure and contents</a></li>
    <li><a href="#data">Data</a></li>
  </ol>
</details>

<!-- OFFICIAL DESCRIPTION FROM INSTRUCTOR -->
## Official description from instructor

### Finding text using edge detection

The purpose of this assignment is to use computer vision to extract specific features from images. In particular, we're going to see if we can find text. We are not interested in finding whole words right now; we'll look at how to find whole words in a coming class. For now, we only want to find language-like objects, such as letters and punctuation.

Download and save the image at the link below:

https://upload.wikimedia.org/wikipedia/commons/f/f4/%22We_Hold_These_Truths%22_at_Jefferson_Memorial_IMG_4729.JPG

Using the skills you have learned up to now, do the following tasks:

* Draw a green rectangular box to show a region of interest (ROI) around the main body of text in the middle of the image. Save this as __image_with_ROI.jpg.__
* Crop the original image to create a new image containing only the ROI in the rectangle. Save this as __image_cropped.jpg.__
* Using this cropped image, use Canny edge detection to 'find' every letter in the image
* Draw a green contour around each letter in the cropped image. Save this as __image_letters.jpg__

__TIPS__

* Remember all of the skills you've learned so far and think about how they might be useful
* This means: colour models; cropping; masking; simple and adaptive thresholds; binerization; mean, median, and Gaussian blur.
* Experiment with different approaches until you are able to find as many of the letters and punctuation as possible with the least amount of noise. You might not be able to remove all artifacts - that's okay!

__Bonus challenges__

* If you want to push yourself, try to write a script which runs from the command line and which takes any similar input (an image containing text) and produce a similar output (a new image with contours drawn around every letter).

__General instructions__

* For this exercise, you can upload either a standalone script OR a Jupyter Notebook
* Save your script as edge_detection.py OR edge_detection.ipynb
* If you have external dependencies, you must include a requirements.txt
* You can either upload the script here or push to GitHub and include a link - or both!
* Your code should be clearly documented in a way that allows others to easily follow along
* Similarly, remember to use descriptive variable names! A name like cropped is more readable than crp.
* The filenames of the saved images should clearly relate to the original image

__Purpose__

This assignment is designed to test that you have a understanding of:

* how to use a variety of image processing steps;
* how to perform edge detection;
* how to combine these skills in order to find specific features in an image

<!-- HOW TO RUN -->
## How to run

__NOTICE:__ To run the assignment, you need to have configured and activated your virtual environment. See the main [README](https://github.com/JohanHorsmans/cds-visual-exam-2021/blob/main/README.md) for a guide on how to do this.

Go through the following steps to run assignment 3:
```bash
cd {root directory (i.e. cds-visual-exam-2021}
cd assignment_3
python3 edge_detection.py
```
Type: ```python3 edge_detection.py -h``` for a detailed guide on how to specify script-parameters. 

<!-- REPOSITORY STRUCTURE AND CONTENTS -->
## Repository structure and contents

This repository contains the following folders:

|Folder|Description|
|:--------|:-----------|
```data/``` | Folder containing data for assignment 3

Furthermore, it holds the following files:
|File|Description|
|:--------|:-----------|
```edge_detection.py``` | The python script for the assignment
```README.md``` | The README file that you are currently reading.

<!-- DATA -->
## Data

The data-folder contains the following files:

|File|Description|
|:--------|:-----------|
WHTT.jpg | An image of a wall with the declaration of independence inscribed. Default image for the script.
Pure_text.png | An image with text saying "Pure Text". Can be used to test the --CUSTOM argument in the function.

<br />
<p align="center">
  <a href="https://github.com/JohanHorsmans/cds-visual-exam-2021">
    <img src="../README_images/logo_au.png" alt="Logo" width="300" height="102">
  </a>
