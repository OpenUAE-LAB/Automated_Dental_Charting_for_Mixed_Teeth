## Introduction

This repository contains the complete implementation used in our manuscript on automated pediatric dental tooth detection and charting from intraoral videos. It includes training and inference scripts, configuration files, and a small example dataset provided solely for reproducibility and pipeline demonstration.
The repository's structure is as follows: 

    .
    ├── data_sample/
    │   ├── train/
    │   │   ├── images/
    │   │   └── labels/
    │   ├── val/
    │   │   ├── images/
    │   │   └── labels/
    │   └── test/
    │       ├── images/
    │       └── labels/
    │
    ├── config_2.yaml
    ├── Main_ModelTraining.py
    ├── requirements.txt
    └── README.md

## Example Dataset (Reproducibility Only)
Due to ethical and privacy constraints associated with pediatric intraoral imaging, the original clinical dataset used in the manuscript cannot be publicly released.
To support reproducibility, this repository includes a small example dataset composed of publicly available adult dental images that have been manually annotated by the authors to match the YOLO annotation format.

⚠️ Important Notes
- The images in data_sample/ are NOT pediatric data
- They are NOT used for training, validation, or evaluation in the paper
- They are provided only to demonstrate:
  - data formatting
  - annotation structure
  - end-to-end training and inference pipeline

⚠️ No performance metrics reported in the paper are derived from this dataset.

### This repository includes a small subset of images derived from the publicly available dataset:
- Dataset:Teeth or Dental image dataset 
- Source: https://data.mendeley.com/datasets/6zsnhrds9t/1  
- License: Creative Commons Attribution 4.0 International (CC BY 4.0)

These images are provided for reproducibility and demonstration only, are not used for model training or evaluation, and have been annotated by the authors of this paper for YOLO formatting.

