# Functions for loading data
from glob import glob
import xarray as xr
import xeofs as xe
def load_coarse_gsam_w():
    path = '/Users/pedro/Datasets/DYAMOND/gSAM/tropical_northwest_pacific/coarsened/*.wa_*.nc'
    files = sorted(glob(path))
    w = xr.concat(
        [xr.open_dataarray(_) for _ in files],
        dim='time'
    )
    return w

def load_gsam_reference_profiles():
    file = '/Users/pedro/Datasets/DYAMOND/gSAM/gsam_z_p_rho_reference.nc'
    return xr.open_dataset(file)

def load_gsam_eofs_pcs():
    file = '/Users/pedro/scale_interaction_in_gsam/data/gsam_coarse_eofs_pcs.nc'
    model = xe.single.EOF.load(file, engine='netcdf4')
    return model

def load_coarse_era5_w():
    path = '/Users/pedro/Datasets/DYAMOND/OBS/ERA5/tropical_northwest_pacific/coarsened/*_w*.nc'
    files = sorted(glob(path))
    w = xr.concat(
        [xr.open_dataarray(_) for _ in files],
        dim='time'
    )
    return w

def load_era5_eofs_pcs():
    file = '/Users/pedro/scale_interaction_in_gsam/data/era5_coarse_eofs_pcs.nc'
    model = xe.single.EOF.load(file, engine='netcdf4')
    return model