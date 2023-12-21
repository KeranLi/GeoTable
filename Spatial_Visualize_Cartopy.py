# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------------ #
# Author: Keran Li, Nanjing University, keranli98@outlook.com
# This module is mainly designed to input must information
# Use add parse to run code on the terminal
# ------------------------------------------------------------------------------------ #

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib.colors as colors
import cartopy.crs as ccrs
import cartopy.feature as cfeature

def plot_age_map(lon, lat, age, figsize, dpi):
    # 创建地图
    fig = plt.figure(figsize=figsize, dpi=dpi)
    ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())
    ax.set_global()

    # 添加经纬度网格线
    ax.gridlines(draw_labels=True, linewidth=0.5, color='gray', alpha=0.5, linestyle='--')

    # 添加地图特征
    ax.add_feature(cfeature.LAND, edgecolor='black')
    ax.add_feature(cfeature.OCEAN)
    ax.add_feature(cfeature.COASTLINE)

    # 根据age数据设置点的颜色和大小
    cmap = cm.get_cmap('coolwarm')
    sc = ax.scatter(lon, lat, c=age, cmap=cmap, s=25, edgecolor='black', linewidths=0.5)

    # 添加颜色条
    cbar = plt.colorbar(sc, shrink=0.8)
    cbar.set_label('Age')

    plt.show()

def plot_age_map_by_period(lat, lon, age, figsize, dpi, period):
    
    # 定义地质时代与年龄的映射关系
    geological_period = {
        (0, 2.56): 'Quaternary',
        (2.56, 23.03): 'Neogene',
        (23.03, 66.0): 'Paleogene',
        (66.0, 145.0): 'Cretaceous',
        (145.0, 201.4): 'Jurassic',
        (201.4, 251.902): 'Triassic',
        (251.092, 298.9): 'Permian',
        (298.9, 358.9): 'Carboniferous',
        (358.9, 419.2): 'Devonian',
        (418.2, 443.8): 'Silurian',
        (443.8, 485.4): 'Ordovician',
        (485.4, 538.9): 'Cambrian',
        (538.9, 2500): 'Proterozoic',
        (2500, 4031): 'Archean',
        (4031, 4567): 'Hadean'
    }
    
    # 根据地质时代获取年龄范围
    age_range = None
    for key, value in geological_period.items():
        if value == period:
            age_range = key
            break
    if age_range is None:
        print(f'Error: period "{period}" not found in geological_period')
        return

    # 根据年龄范围过滤数据
    mask = (age >= age_range[0]) & (age < age_range[1])
    lat = lat[mask]
    lon = lon[mask]

    # 创建地图
    fig = plt.figure(figsize=figsize, dpi=dpi)
    ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())
    ax.set_global()

    # 添加经纬度网格线
    ax.gridlines(draw_labels=True, linewidth=0.5, color='gray', alpha=0.5, linestyle='--')

    # 添加地图特征
    ax.add_feature(cfeature.LAND, edgecolor='black')
    ax.add_feature(cfeature.OCEAN)
    ax.add_feature(cfeature.COASTLINE)

    # 根据age数据设置点的颜色和大小
    cmap = cm.get_cmap('coolwarm')
    sc = ax.scatter(lon, lat, c=age, cmap=cmap, s=25, edgecolor='black', linewidths=0.5)

    # 添加颜色条
    cbar = plt.colorbar(sc, shrink=0.8)
    cbar.set_label('Age')

    plt.show()