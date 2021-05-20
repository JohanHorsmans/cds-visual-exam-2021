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
    <a href="https://github.com/JohanHorsmans/cds-visual-exam-2021/blob/main/Visual_Analytics_Exam.pdf"><strong>Link to PDF with all portfolio descriptions »</strong></a>
    <br />
  </p>
</p>

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#official-description-from-instructor">Official description from instructor</a></li>
    <li><a href="#methods">Methods</a></li>
    <li><a href="#how-to-run">How to run</a></li>
    <li><a href="#repository-structure-and-contents">Repository structure and contents</a></li>
    <li><a href="#data">Data</a></li>
    <li><a href="#discussion-of-results">Discussion of results</a></li>
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

<!-- METHODS -->
## Methods

The problem in this assignment relates to preprocessing images and then extracting specific features/edges in the image. To solve the task, I started by preprocessing the image with various cv2-functions. To find the edges, I used the _findContours_-function from cv2. As an added bonus, I also used pytesseract to convert the text in the image to a string and print the text in the terminal. To solve the bonus assignment, I used argparse to enable the user to specify arguments from the terminal. With argparse, I made it possible for the user to specify their own image path with an argument called --image_path. In the data-folder in the repository, I included an image titled "Pure_text.png" which the user can use to test the --image_path argument.

<!-- HOW TO RUN -->
## How to run

__NOTICE:__ To run the assignment, you need to have configured and activated your virtual environment. See the main [README](https://github.com/JohanHorsmans/cds-visual-exam-2021/blob/main/README.md) for a guide on how to do this.

Go through the following steps to run assignment 3:
```bash
cd {root directory (i.e. cds-visual-exam-2021}
cd assignment_3
python3 edge_detection.py
```
__You can specify the following optional arguments from the terminal:__
```bash
-i 
--image_path
default =  os.path.join("data","WHTT.jpg")
type = str
help = string, path to input file. Be weary of difference in operating systems in terms of spcifying path with  "/" or "\".
```
You can also type: ```python3 edge_detection.py -h``` for a detailed guide on how to specify script-parameters. 

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
Pure_text.png | An image with text saying "Pure Text". Can be used to test the --image_path argument in the script.

<!-- DISCUSSION OF RESULTS -->
## Discussion of results

The contours drawn on the image were quite good (see _figure 1_). Nonetheless, we can see that it has not
succeeded in exclusively capturing the letters since it also has drawn contours on the brick-lines in the wall
where the text is inscribed. When testing the --image_path argument, I experimented with drawing contours on
a lot of different images where it achieved similar levels of performance. As such, I believe that my
solution is quite robust. Furthermore, my script is fairly successful in converting the image to a string as
seen by the following output where there are only a few errors:

_"we hold these truths to be self evident that all men are created equal that they are endowed by their creator
with certain inalienable rights among these are life liberty and the pursuit of happiness that to securethese
rights governments are instituted among men we solemnly publish and declare that these colonies are and of
right ought to be free and independent states and for the support of this declaration with a firm reliance on
the protection of divine providence we mutually pledge our lives our fortunes and our sacred honour we"._


<br />
<p align="center">
  <a href="https://github.com/JohanHorsmans/cds-visual-exam-2021">
    <img src="../README_images/image_letters.jpg" alt="Logo">
  </a>
<p align="center">
Figure 1: The final contours drawn on the image.

<br />
<p align="center">
  <a href="https://github.com/JohanHorsmans/cds-visual-exam-2021">
    <img src="../README_images/logo_au.png" alt="Logo" width="300" height="102">
  </a>
