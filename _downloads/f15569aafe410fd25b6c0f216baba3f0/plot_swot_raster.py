#!/usr/bin/env python
# coding: utf-8

"""
Read and plot a SWOT-HR Raster products 
==========================================================================

In this example, we show how to read the SWOT-HR raster 100m or 250m netcdf products with xarray and how to represent a variable on a map with cartopy.
"""

# %%
# Libraries

import xarray as xr
import rioxarray
from pyproj import CRS
import os
import numpy as np
import matplotlib.pyplot as plt


# %%
# 1. Read a SWOT-HR Raster netcdf product with xarray
# ===================================================

dir_swot = "_data"
file_swot_raster = os.path.join(
                          dir_swot,
                          "SWOT_L2_HR_Raster_250m_UTM30T_N_x_x_x_001_042_036F_20220402T112059_20220402T112119_Dx0000_01.nc",
                          )
# read data with xarray
xr_swot_raster = xr.open_dataset(file_swot_raster)
# force xarray to acknowledge the CRS 
xr_swot_raster.rio.set_crs(
    CRS.from_user_input(xr_swot_raster.crs.projected_crs_name).to_epsg(), 
    inplace=True,
    )

# %%
# Should you want to quickly see what the data looks like, just use the following line. Lower in the example we will try to have something fancier.
xr_swot_raster.wse.plot(cmap='cividis')


# %%
# 2. Plot data on maps with cartopy
# =================================

# %%
# let us create a little function to simplify the mapping part
import cartopy.crs as ccrs
import cartopy.feature as cfeature


def customize_map(ax, cb, label, crs=ccrs.PlateCarree()):
    """This function customizes a map with projection and returns the plt.axes instance"""

    ax.gridlines(
        crs=crs,
        draw_labels=True,
        color='.7',
        alpha=.6,
        linewidth=.4,
        linestyle='-',
        )
    
    # add a background_map (default, local image, WMTS...read the doc)
    # ax.stock_img()

    # add a labeled colorbar
    plt.colorbar(
        cb,
        ax=ax,
        orientation='horizontal',
        shrink=0.6,
        pad=.05,
        aspect=40,
        label=label)

    return ax

# %%
# Create Figure and Axes and plot data with pcolor

crs = ccrs.PlateCarree()
fig, axs = plt.subplots(
    nrows=1,ncols=2,
    subplot_kw={'projection': crs},
    figsize=(16,9),
    frameon=True,
    )

# 1. plot Water Surface Elevation on map
# plot data on the map with pcolor function
cb0 = axs[0].pcolor(
    xr_swot_raster.longitude,
    xr_swot_raster.latitude,
    xr_swot_raster.wse,
    transform=crs,
    cmap='cividis',
    )
# customize plot with pre-defined function
customize_map(axs[0], cb0, "Water Surface Elevation (m)")

# 2. plot Water Fraction on map
cb1 = axs[1].pcolor(
    xr_swot_raster.longitude,
    xr_swot_raster.latitude,
    xr_swot_raster.water_frac*100,
    transform=crs,
    cmap='BuPu',
    vmin=0,
    vmax=100,
    )
# customize plot with pre-defined function
customize_map(axs[1], cb1, "Water Fraction (%)")

fig.show()

# %%
#


