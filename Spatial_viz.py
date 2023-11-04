# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------------ #
# Author: Keran Li, Nanjing University, keranli98@outlook.com
# This module is mainly designed to input must information
# Use add parse to run code on the terminal
# ------------------------------------------------------------------------------------ #

import pandas as pd
import numpy as np
import pygmt
import argparse
from tqdm import tqdm

def load_data(filepath):
    """加载数据"""
    df = pd.read_excel(filepath)
    lat = np.round(df['Latitud'].dropna().values, 2)
    lon = np.round(df['Logitud'].dropna().values, 2)
    return lat, lon

def create_basemap(region):
   """创建基本地形图"""
   grid = pygmt.datasets.load_earth_relief(resolution='01m', region=region) 
   fig = pygmt.Figure()
   fig.grdimage(grid=grid, projection='M15c', frame='a', cmap='geo')
   return fig

def plot_points(fig, lon, lat):
    """绘制点"""
    fig.plot(x=lon, y=lat, style='c0.5c', color='red', pen='black')
    
def add_features(fig, region):
    """添加地名等要素"""
    fig.colorbar(frame=["a2000", "x+lElevation", "y+lm"])
    
def save_map(fig, filename):
    """保存结果"""
    fig.savefig(filename)

# 主程序逻辑
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', required=True, help='input data file')
    parser.add_argument('-o', '--output', required=True, help='output image file')
    args = parser.parse_args()

    lat, lon = load_data(args.input) 
    region = [70, 140, 0, 55]
    
    fig = create_basemap(region)

    # 用tqdm显示循环进度
    for _ in tqdm(range(10)):
        plot_points(fig, lon, lat) 

    add_features(fig, region)
    save_map(fig, args.output)