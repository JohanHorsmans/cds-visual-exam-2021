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
      <a href="#portfolio-assignments">Portfolio assignments</a>
      <ul>
        <li><a href="#assignment-3---edge-detection">Assignment 3 - Edge detection</a></li>
        <li><a href="#assignment-4---logistic-regression-and-neural-network-benchmark-mnist-classification">Assignment 4 - Logistic Regression and Neural Network benchmark mnist classification</a></li>
        <li><a href="#assignment-5---cnn-classification-of-impressionist-paintings">Assignment 5 - CNN classification of impressionist paintings</a></li>
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
* Assignment 3 - _Edge detection_
* Assignment 4 - _Logistic Regression and Neural Network benchmark mnist classification_
* Assignment 5 - _CNN classification of impressionist paintings_
* Self-assigned - _something fucking sick_

<!-- HOW TO RUN -->
## How to run

To run the assignments, you need to go through the following steps in your bash-terminal to configure a virtual environment with the needed prerequisites for all assignments:

__MAC/LINUX/WORKER02__
```bash
git clone https://github.com/JohanHorsmans/cds-visual-exam-2021.git
cd cds-visual
bash ./create_vis_venv.sh
```
__WINDOWS:__
```bash
git clone https://github.com/JohanHorsmans/cds-visual-exam-2021.git
cd cds-visual
bash ./create_vis_venv_win.sh
```

<!-- REPOSITORY STRUCTURE AND CONTENTS -->
## Repository structure and contents

This repository contains the following folders:

|Folder|Description|
|:--------|:-----------|
```data/```| Folder containing the data used for the assignments
```assignment_.*/``` | Folder containing code for the four assignments
```utils``` | Folder containing utility functions written by our teacher, [Ross Deans Kristensen-McLachlan](https://pure.au.dk/portal/en/persons/ross-deans-kristensenmclachlan(29ad140e-0785-4e07-bdc1-8af12f15856c).html), which are employed in some of the assignments.

Furthermore, it holds the following files:
|File|Description|
|:--------|:-----------|
```./create_vis_venv.*.sh``` | A bash script that generates a new virtual environment with all the packages specified in the ```requirements.txt```-file.
```requirements.txt``` | A txt-file containing a list of the packages (and versions) that are needed for the virtual environment.
```README.md``` | The README file that you are currently reading.

<!-- DATA -->
## Data

The data-folder contains the following files:

|File|Description|
|:--------|:-----------|
flowers | flowers
cf-test | test
mnist | test

<!-- PORTFOLIO ASSIGNMENTS -->
## Portfolio assignments

### Assignment 3 - Edge detection
#### Content of assignment

For more information, see ```assignment_3/README.md```

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

By all means write me, Johan Horsmans, for any questions regarding the repository/assignments. You can contact me on my e-mail horsmans1004@gmail.com or on [Facebook](https://www.facebook.com/johan.horsmans/).

<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements
* [Ross Dean McLachlan](https://pure.au.dk/portal/en/persons/ross-deans-kristensenmclachlan(29ad140e-0785-4e07-bdc1-8af12f15856c).html) - Our teacher for the Visual Analytics course
* [Emil Jessen](https://github.com/emiltj) - My partner for the self-assigned project with whom I have also collaborated in creating this README-file structure.
