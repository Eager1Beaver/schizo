# Schizo
### Overiew
This project focuses on exploring the effect of various preprocessing and data augmentation methods on thre results of detecting schizophrenia from Magnetic Resonance (MR) images. The aim of this exploration is to address the existing ambiguity in how MR images are preprocessed before training, as most authors in literature perform preprocessing in MATLAB without clear instructions for reproducibility.

## Project Data:
Find the raw data at [SchizConnect] {http://schizconnect.org/}
The data comes as 3-dimensional MRI volumes in NifTI format


![Sample volume](tools/sample_volume.png)




## Project Workflow:
Data Exploration >> [Preprocessing] (src/utils/preprocess.py) & [Augmentation] (src/augmentation.py) >> [Feature Extraction & Training] (src/models/models.py) >> Visualizing training results

## Repository Structure
C:.
+---src
   +---models
   +---paper
   ª   +---figs
   +---utils
       +---__pycache__
+---tests
+---tools

## To run the project follow this commands:
All command should run under project root/working-directory
```bash 
#install Virtualenv is - a tool to set up your Python environments
pip install virtualenv
#create virtual environment (serve only this project):
python -m venv venv
#activate virtual environment
.\venv\Scripts\activate
+ (venv) should appear as prefix to all command (run next command just after activating venv)
#update venv's python package-installer (pip) to its latest version
python.exe -m pip install --upgrade pip
#install projects packages (Everything needed to run the project)
pip install -e .
#install dev packages (Additional packages for linting, testing and other developer tools)
pip install -e .[dev]
``` 