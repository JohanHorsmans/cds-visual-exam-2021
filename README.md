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
    <li><a href="#project-info">Project info</a></li>
    <li><a href="#how-to-run">How to run</a></li>
    <li><a href="#repository-structure-and-contents">Repository structure and contents</a></li>
    <li><a href="#data">Data</a></li>
    <li>
      <a href="#portfolio-assignments">Portfolio assignment</a>
      <ul>
        <li><a href="#assignment-2">Assignment 2</a></li>
        <li><a href="#assignment-4">Assignment 4</a></li>
        <li><a href="#assignment-5">Assignment 5</a></li>
        <li><a href="#self-assigned-assignment">self-assigned assignment</a></li>
      </ul>
    </li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>


<!-- PROJECT INFO -->
## Project info

This repository houses the exam of _Johan Kresten Horsmans (AU ID: 618771)_ for the course [_Visual Analytics_](https://kursuskatalog.au.dk/en/course/101992/Visual-Analytics), as part of the bachelor's elective [_Cultural Data Science_](https://bachelor.au.dk/en/supplementary-subject/culturaldatascience/) at Aarhus University. The repository consists of 4 projects: three class assignments and one self-assigned project. The following README details how to run the code and contains a thorough explanation of how the repository is structured.

The assignments included in this portfolio are the following:
* Assignment 2 - Image search 
* Assignment 4 - Logistic Regression and Neural Network benchmark mnist classification
* Assignment 5 - CNN classification of impressionist paintings
* Self-assigned - * *

<!-- HOW TO RUN -->
## How to run

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

<!-- REPOSITORY STRUCTURE AND CONTENTS -->
## Repository structure and contents

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

<!-- DATA -->
## Data
* flowers
* cf-test
* mnist

<!-- PORTFOLIO ASSIGNMENTS -->
## Portfolio assignments

### Assignment 2 - Image search
#### Content of assignment
This assignment contains the following:


For more information, see ```assignment_2/README.md```

### Assignment 4 - Logistic Regression and Neural Network benchmark mnist classification

For more information, see ```assignment_4/README.md```

### Assignment 5 - CNN classification of impressionist paintings

For more information, see ```assignment_5/README.md```

### Self-assigned assignment

For more information, see ```assignment_self_assigned/README.md```

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
* [Emil Jessen](https://github.com/emiltj) - My partner for the self-assigned project and with whom I have collaborated in creating this README-file structure.
