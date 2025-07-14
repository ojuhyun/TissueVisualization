{\rtf1\ansi\ansicpg1252\cocoartf2759
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;\f1\fnil\fcharset0 AppleColorEmoji;\f2\fnil\fcharset129 AppleSDGothicNeo-Regular;
}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 # Synthetic Image Generator for Multiplexed Tissue Imaging\
\
This repository provides a Python script to generate synthetic dot-based images of cell identities using single-cell spatial data and segmentation masks. The tool was developed for visualizing cell-type distributions in multiplexed tissue imaging data\
\
## Overview\
\
The `create_graphics` function takes segmentation masks and annotated single-cell data to generate synthetic TIF images for each field of view (FOV), where each cell is plotted as a dot and color-coded by identity.\
\
## 
\f1 \uc0\u55357 \u56513 
\f0  Repository Structure\
\
\pard\pardeftab720\partightenfactor0

\f2 \cf0 \expnd0\expndtw0\kerning0
\'a6\'a7
\f0 \uc0\u9472 \u9472  generate_synthetic_images.py # Main script with the create_graphics() function\

\f2 \'a6\'a7
\f0 \uc0\u9472 \u9472  README.md # This file\
\uc0\u9492 \u9472 \u9472  requirements.txt # Python dependencies\
\
\
\
## Requirements\
\
Install dependencies via pip:\
\
```bash\
pip install -r requirements.txt\
\
\
## Usage\
from generate_synthetic_images import create_graphics\
\
# Required inputs\
parent_dir = '/path/to/root_folder'\
sample_name = 'Sample123'\
fov = 's5'  # Field of view\
final_TAM_df = pd.read_csv('annotated_cells.csv')  # Your single-cell data\
\
# Run the function\
create_graphics(parent_dir, sample_name, fov, final_df)\
}