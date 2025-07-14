# Synthetic Image Generator for Multiplexed Tissue Imaging

This repository provides a Python script to generate synthetic dot-based images of cell identities using single-cell spatial data and segmentation masks. The tool was developed for visualizing cell-type distributions in multiplexed tissue imaging data

## Overview

The `create_graphics` function takes segmentation masks and annotated single-cell data to generate synthetic TIF images for each field of view (FOV), where each cell is plotted as a dot and color-coded by identity.

## Repository Structure

├── generate_synthetic_images.py # Main script with the create_graphics() function
├── README.md # This file
└── requirements.txt # Python dependencies


## Requirements

Install dependencies via pip:

bash
pip install -r requirements.txt

## Usage
from generate_synthetic_images import create_graphics

# Required inputs
parent_dir = '/path/to/root_folder'
sample_name = 'Sample123'
fov = 's5'  # Field of view
final_df = pd.read_csv('annotated_cells.csv')  # Your single-cell data

# Run the function
create_graphics(parent_dir, sample_name, fov, final_df)
