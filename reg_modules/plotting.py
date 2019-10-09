from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import xarray as xr
import SimpleITK as sitk
import panel as pn
import holoviews as hv
from holoviews import opts
from functools import reduce
from holoviews.operation.datashader import datashade, shade, dynspread, rasterize
from holoviews.streams import RangeXY
hv.extension('bokeh')

def patient_reg_comparison(fixed, moving_init, moving_final, grid=None):
    '''Comparing 3 images at once for alpha blending.  Expects sitk input format.'''

    imopts = {'tools': ['hover'], 'width': 500, 'height': 500}
    hv_fixed = hv.Image(sitk.GetArrayFromImage(fixed)).opts(**imopts, cmap='Blues')
    hv_moving_init = hv.Image(sitk.GetArrayFromImage(moving_init)).opts(**imopts, cmap='Greens')
    hv_moving_final = hv.Image(sitk.GetArrayFromImage(moving_final)).opts(**imopts, cmap='Reds')
    if grid:
        hv_grid = hv.Image(sitk.GetArrayFromImage(grid)).opts(**imopts, cmap='Greys_r')

    # Make an alpha slider
    slider1 = pn.widgets.FloatSlider(start=0, end=1, value=0.0, name='moving_init')
    slider2 = pn.widgets.FloatSlider(start=0, end=1, value=0.0, name='moving_final')
    # Plot the slider and the overlayed images using the '*' operator
    if grid:
        return pn.Column(slider1, slider2,
                         rasterize(hv_fixed) *
                         rasterize(hv_moving_init.apply.opts(alpha=slider1.param.value)) *
                         rasterize(hv_moving_final.apply.opts(alpha=slider2.param.value)) +
                         rasterize(hv_grid))
    else:
        return pn.Column(slider1, slider2,
                         rasterize(hv_fixed) *
                         rasterize(hv_moving_init.apply.opts(alpha=slider1.param.value)) *
                         rasterize(hv_moving_final.apply.opts(alpha=slider2.param.value)))
