# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------------ #
# Author: Keran Li, Nanjing University, keranli98@outlook.comy
# This module is mainly designed to load, merge and export excel files
# ------------------------------------------------------------------------------------ #

import os
import pandas as pd
from tqdm import tqdm
import time

def import_merge_data(folder_path):

    # Set up a new df to store data
    combined_data = pd.DataFrame()
    # Calculate the running time/Gain the start time point
    start_time = time.time() 

    # Loops all excel files in the fold
    for filename in tqdm(os.listdir(folder_path), desc="Merging Excel Files"):
        if filename.endswith('.xlsx'): # Make sure all files are .xlsx type
            file_path = os.path.join(folder_path, filename) # Build full direction
            df = pd.read_excel(file_path) # Load data
            combined_data = pd.concat([combined_data, df], ignore_index=True) # Merge data
    
    # Calculate the running time/Gain the end time point
    end_time = time.time()
    # Calculate the running time/Gain the total time
    total_time = end_time - start_time
    # Print the total time
    print(f"Total time taken: {total_time} seconds")
    return combined_data

def export_combined_data(combined_data, output_path):
    combined_data.to_excel(output_path, index=False)
    print("Excel files merged and exported successfully.")