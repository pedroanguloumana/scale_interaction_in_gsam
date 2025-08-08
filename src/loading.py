# Functions for loading data
from glob import glob
import xarray as xr
import xeofs as xe
# Change below directory to desired location
#
BASE_DIRECTORY = '/Users/pedro/scale_interaction_in_gsam/data'

def load_coarse_gsam_w():
    path = BASE_DIRECTORY + '/raw_gsam_data/coarsened/*.wa_*.nc'
    files = sorted(glob(path))
    w = xr.concat(
        [xr.open_dataarray(_) for _ in files],
        dim='time'
    )
    return w

def load_gsam_reference_profiles():
    file = BASE_DIRECTORY + '/gsam_z_p_rho_reference.nc'
    return xr.open_dataset(file)

def load_gsam_eofs_pcs():
    file = BASE_DIRECTORY + '/gsam_coarse_eofs_pcs.nc'
    model = xe.single.EOF.load(file, engine='netcdf4')
    return model

def load_coarse_era5_w():
    path = BASE_DIRECTORY + '/raw_era5_data/coarsened/*_w*.nc'
    files = sorted(glob(path))
    w = xr.concat(
        [xr.open_dataarray(_) for _ in files],
        dim='time'
    )
    return w

def load_era5_eofs_pcs():
    file = BASE_DIRECTORY + '/era5_coarse_eofs_pcs.nc'
    model = xe.single.EOF.load(file, engine='netcdf4')
    return model

def get_raw_gsam_variable_files(var: str):
    path = BASE_DIRECTORY + f'/raw_gsam_data/{var}/*.nc'
    files = sorted(glob(path))
    return files

def get_daily_combined_2d_gsam_files():
    path = BASE_DIRECTORY + f'/raw_gsam_data/2d/daily_2d/*202002*.nc'
    files = sorted(glob(path))
    return files

def load_phase_composite_anomaly(variable, phase):
    path = BASE_DIRECTORY + f'/phase{phase}_composite_anomaly_{variable}.nc'
    return xr.open_dataarray(path)

def load_phase_composite_mean(variable, phase):
    path = BASE_DIRECTORY + f'/phase{phase}_composite_mean_{variable}.nc'
    return xr.open_dataarray(path)
