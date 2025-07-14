"""
Synthetic Image Generator for Multiplexed Tissue Imaging Data

Author: Juhyun Oh
Center for Systems Biology
Massachusetts General Hospital

Description:
This script generates synthetic dot images of cell identities based on single-cell spatial data
and segmentation masks. It assigns colors to different immune cell types and saves output images
per field of view (FOV).
"""

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import skimage.io
from PIL import Image

def create_graphics(parent_dir, sample_name, fov, final_TAM_df, plot=False):
    """
    Generate a synthetic image of a single FOV with individual cells colored as dots 
    according to their identity.

    Parameters
    ----------
    parent_dir : str
        Root directory containing segmentation and output folders.
    sample_name : str
        Name of the sample (used in folder and file names).
    fov : str or int
        Field of view identifier (e.g., 's1').
    final_df : pd.DataFrame
        DataFrame containing single-cell information including 'FOV', 'ObjectNumber', 
        'Identity', and 'Location_Center_X/Y'.
    plot : bool, optional
        If True, displays the plot before saving. Default is False.

    Returns
    -------
    None
        Saves TIF images in the output directory.
    """
    
    # Define directories
    img_dir = os.path.join(parent_dir, 'MacMonoMicroglia')
    graph_dir = os.path.join(img_dir, f"SyntheticImages/{sample_name}")
    os.makedirs(graph_dir, exist_ok=True)

    # Load cell segmentation mask
    mask_path = os.path.join(img_dir, f'{sample_name}/{sample_name}_w1_{fov}_t1_segmentation.tiff')
    cell_mask = skimage.io.imread(mask_path)
    iden_image = np.zeros(cell_mask.shape)

    # Filter cells for the current FOV
    df_loc = final_df.loc[final_df['FOV'] == fov]
    iden_list = df_loc['Identity'].unique()
    iden_dict = {iden: num for num, iden in enumerate(iden_list, start=1)}

    # Populate identity image with numerical labels
    for _, row in df_loc.iterrows():
        iden_image[cell_mask == row['ObjectNumber']] = iden_dict[row['Identity']]

    # Define color dictionary (binary example)
    ImmColorDict2 = {
        'NaN': [0.827, 0.827, 0.827],
        'Stroma': [0.827, 0.827, 0.827],
        'Tumor': [0.502, 0.502, 0.502],
        'Monocyte_Stroma': [0.678, 0.643, 0.322],
        'Monocyte_Microglia_Stroma': [0.678, 0.643, 0.322],
        'Macrophage_Stroma': [0.886, 0.502, 0.463],
        'Macrophage_Monocyte_Stroma': [0.886, 0.502, 0.463],
        'Microglia_Stroma': [0.392, 0.722, 0.651]
    }

    # Create dot-based identity plot
    fig, ax = plt.subplots()
    for iden, color in ImmColorDict2.items():
        dff = df_loc[df_loc['Identity'] == iden]
        ax.scatter(dff['Location_Center_Y'], dff['Location_Center_X'],
                   color=color, s=100, alpha=0.95, edgecolors='none')

    ax.set_xlim([-10, iden_image.shape[1] + 10])
    ax.set_ylim([iden_image.shape[0] + 10, -10])
    ax.set_aspect('equal')
    ax.axis('off')

    out_path = os.path.join(graph_dir, f'{sample_name}_{fov}_CellTypeCalling_dot.TIF')
    fig.savefig(out_path, bbox_inches='tight', pad_inches=0)
    if plot:
        plt.show()
    plt.close(fig)

    # Load and rotate the saved image
    original_img = Image.open(out_path)
    rotated_img = original_img.transpose(Image.FLIP_LEFT_RIGHT).rotate(90)
    rotated_img.save(os.path.join(graph_dir, f'{sample_name}_{fov}_CellTypeCalling_dot_rotate.TIF'))
