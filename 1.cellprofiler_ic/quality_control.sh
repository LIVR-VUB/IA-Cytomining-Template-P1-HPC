#!/bin/bash

# initialize the correct shell for your machine to allow conda to work (see README for note on shell names)
conda init bash
# activate the main conda environment
conda activate cytomining_a

# go into the image_quality_control directory
cd image_quality_control

# Create the scripts directory if it doesn't exist
mkdir -p scripts

# Convert all notebooks to Python scripts into the scripts folder
jupyter nbconvert --to script --output-dir=scripts/ *.ipynb

# run the image quality control scripts (python)
python scripts/0.whole_image_qc.py # Comment out unless you have made changes to the QC pipeline
#python scripts/1.evaluate_qc.py

# deactivate the main conda environment
conda deactivate

# activate the R specific conda environment (from 4.analyze_data)
#conda activate r_analysis_nf1

# run the image quality control R script
#Rscript scripts/2.qc_report.r


