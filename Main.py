# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------------ #
# Author: Keran Li, Nanjing University, keranli98@outlook.comy
# This module is mainly designed to input must information
# Use add parse to run code on the terminal
# ------------------------------------------------------------------------------------ #

import argparse
from TableProcess import import_merge_data, export_combined_data

def main():

    # Set up the argparse interprets
    parser = argparse.ArgumentParser(description="Combine and export data from multiple Excel files")

    # Add parameters
    """
    --input_folder, the folder that you want to merge
    --output_file, the folder that you want to store results
    """
    parser.add_argument('--input_folder', '-i', type=str, default='./experimental_datasets/',
                        help="Input files' directory")
    parser.add_argument('--output_file', '-o', type=str, default='./results/experimental_combined_data.xlsx',
                        help="Output file's name")
    
    # Parameters backles up
    args = parser.parse_args()

    # Import some pre-defined functions
    combined_data = import_merge_data(args.input_folder)
    export_combined_data(combined_data, args.output_file)

    print(f"Exported data to: {args.output_file}")

if __name__ == '__main__':
    main()