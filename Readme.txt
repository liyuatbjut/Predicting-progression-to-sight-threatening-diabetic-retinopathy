This repository contains the source code for the manuscript "Predicting progression to sight-threatening diabetic retinopathy based on fundus photography using deep learning," submitted to Journal of Imaging Informatics in Medicine .

The project develops a deep learning model to predict the progression of diabetic retinopathy to its sight-threatening stages (STDR) using fundus photographs.

Repository Structure
The code is organized into several key scripts, each serving a distinct purpose in the model development and analysis pipeline:

File	Description
Mainxy.py	The main script for performing statistical analysis on the dataset and model results.
Train.py	Contains the code for building and training the deep learning prediction model.
Test.py	Used to evaluate the trained model's performance on the hold-out test set.
visualize.py	Generates visualizations for model interpretation (e.g., saliency maps, Grad-CAM, performance plots).
CLAHE.py	A directory containing scripts for pre-processing fundus images using Contrast Limited Adaptive Histogram Equalization (CLAHE) for image enhancement.
Usage

A typical workflow for replicating the study's results would be:

Pre-processing: Enhance the raw fundus images using  CLAHE.py

Training: Execute Train.py to build and train the deep learning model.

Evaluation: Run Test.py to generate predictions and performance metrics on the test set.

Analysis & Visualization: Use Mainxy.py for statistical analysis and visualize.py to create explanatory figures.

Requirements
To run this code, please ensure you have the following dependencies installed. A specific version list can be found in requirements.txt (if provided).

Python 3.7+

PyTorch / TensorFlow (whichever is used in the code)

OpenCV

NumPy

Scikit-learn

Matplotlib / Seaborn

Pillow (PIL)

You can install the necessary packages using:

bash
pip install -r requirements.txt