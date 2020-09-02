# Illustris project
This is the repository for my project thesis at NTNU where I work on the [Illustris](tng-project.org) data. 

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the needed python packages:

```bash
pip install numpy
```
The python packages used in this project are:
- numpy
- matplotlib
- h5py
- six
- pandas

You also need the Jupyter Notebook application
```bash
pip install notebook
```
## Usage

To run the code, first clone the entire repository from github to your local computer.
The python files can then be run directly from the terminal. 

```powershell
cd "..."/illustris-project/src
./myfile.py
```

The jupyter notebooks can be run from the browser by starting the Jupyter Notebook application from the terminal:

```
cd "..."/illustris-project
jupyter notebook
```
NOTE: the python files and the jupyter notebook files use slightly different paths to navigate through the directories, as I run my python files from the top directory, but the jupyter notebook files are run from the src/ folder. Any problems that arise might have to do with this, so please be aware of what is your working directory while running the code.

## Contents

The repository consists of three main folders:
* data/ contains the raw and modified data from the TNG simulations. There may be some large files in this folder.
* fig/ contains the figures produced in the project
* src/ contains the actual python and jupyter notebook scripts

### Data
The data is organised by their respective TNG run, as well as whether or not it is the complete catalogue files. The smaller filtered data that is tailored for each scripts needs are placed in the subfolders `./cutdata/`. The file names should be descriptive of what data they contain.