<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/JohanHorsmans/cds-visual-exam-2021">
    <img src="README_images/computer vision.png" alt="Logo" width="158" height="146">
  </a>
  
  <h1 align="center">Cultural Data Science 2021</h1> 
  <h3 align="center">Visual Analytics Exam</h3> 


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
    <li><a href="#about-the-project">Project Info</a></li>
    <li><a href="#getting-started">How to run</a></li>
    <li><a href="#repository-structure-and-contents">Repository structure & contents</a></li>
    <li>
      <a href="#assignments">Portfolio Assignment</a>
      <ul>
        <li><a href="#assignment-2">Assignment 2</a></li>
        <li><a href="#assignment-4">Assignment 4</a></li>
        <li><a href="#assignment-5">Assignment 5</a></li>
        <li><a href="#self-assigned-assignment">elf-assigned assignment</a></li>
      </ul>
    </li>
    <li><a href="#data">Data</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>


<!-- ABOUT THE PROJECT -->
## About the project

This project contains the exam portofolio coding related to the Spring 2021 module _Visual Analytics_ as part of the bachelor's tilvalg in [_Cultural Data Science_](https://bachelor.au.dk/en/supplementary-subject/culturaldatascience/) at Aarhus University. 
This README contains all the necessary information needed to get an overview of the repository, as well the installation steps required for rerunning the assignments. 

Assignments chosen for this portfolio:
* Assignment 2 - Image search 
* Assignment 4 - Logistic Regression and Neural Network benchmark mnist classification
* Assignment 5 - CNN classification of impressionist paintings
* Self-assigned - * *

<!-- GETTING STARTED -->
## Getting started

For running my scripts I'd recommend following the below steps in your bash-terminal as a setup of the virtual environment needed for all of the individual assignments.

__MAC/LINUX/WORKER02__
```bash
git clone https://github.com/emiltj/cds-visual.git
cd cds-visual
bash ./create_vis_venv.sh
```
__WINDOWS:__
```bash
git clone https://github.com/emiltj/cds-visual.git
cd cds-visual
bash ./create_vis_venv_win.sh
```

<!-- REPOSITORY STRUCTURE -->
## Repository structure

This repository has the following directory structure:

| Column | Description|
|--------|:-----------|
```data/```| Contains the data used in the assignments
```assignment_.*/``` | Contains the 4 assignments
```utils``` | Utility functions written by [Ross](https://pure.au.dk/portal/en/persons/ross-deans-kristensenmclachlan(29ad140e-0785-4e07-bdc1-8af12f15856c).html) which are utilised in some of the scripts

Furthermore it contains the files:
- ```./create_vis_venv.*.sh``` -> Bash scripts that automatically generates a new virtual environment, and install all the packages contained within ```requirements.txt```
- ```requirements.txt``` -> A list of packages along with the versions that work for the scripts
- ```README.md``` -> This very README file

<!-- ASSIGNMENTS -->
## Assignments

### Assignment 2 - Image search
#### Content of assignment
This assignment contains the following:


For more information, see ```assignment_2/README.md```

### Assignment 4 - Logistic Regression and Neural Network benchmark mnist classification

For more information, see ```assignment_4/README.md```

### Assignment 5 - CNN classification of impressionist paintings

For more information, see ```assignment_5/README.md```

### Assignment self-assigned

For more information, see ```assignment_self_assigned/README.md```

<!-- DATA -->
## Data
flowers
cf-test
mnist

<!-- LICENSE -->
## License
Distributed under the [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0). See ```LICENSE``` for more information.

<!-- CONTACT -->
## Contact

Feel free to write me, Johan Horsmans for any questions (also regarding the reviews). 
You can do so on horsmans1004@gmail.com or on [Facebook](https://www.facebook.com/johan.horsmans/).

<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements
* [Python](https://www.rstudio.com/) - Software used for conducting the analysis
* [Ross Dean McLachlan](https://github.com/CDS-AU-DK/) - Our competent instructor for the module on Visual Analytics
* [Emil Jessen](https://github.com/emiltj) - My partner for the final project and with whom I have collaborated in creating this README-file structure.
