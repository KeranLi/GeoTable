# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------------ #
# Author: Keran Li, Nanjing University, keranli98@outlook.comy
# This module is mainly designed to input must information
# ------------------------------------------------------------------------------------ #

from TableProcess import import_merge_data, export_combined_data

folder_path = 'unprocessed_datasets/'  # Input files' direction. Here, we just need to input the fold name because all files in the fold will be input
output_path = 'combined_data.xlsx'  # Output file's direction. Here, the default direction is same with the "Main.py"

# Import and merge data file
combined_data = import_merge_data(folder_path)

# Export data file
export_combined_data(combined_data, output_path)