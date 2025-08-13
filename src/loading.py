# Functions for loading data
from glob import glob
import xarray as xr
import xeofs as xe
# Change below directory to desired location
#
BASE_DIRECTORY = '/Users/pedro/scale_interaction_in_gsam/data'

def load_coarse_gsam_w():
    path = BASE_DIRECTORY + '/raw_gsam_data/coarsened_w/*.wa_*.nc'
    files = sorted(glob(path))
    w = xr.concat(
        [xr.open_dataarray(_) for _ in files],
        dim='time'
    )
    return w

def load_raw_gsam_2d():
    path = BASE_DIRECTORY + f'/raw_gsam_data/2d/daily_2d/*.nc'
    files = sorted(glob(path))
    data = xr.concat(
        [xr.open_dataset(_) for _ in files],
        dim='time'
    )
    return data

def load_gsam_olr_on_1deg():
    path = BASE_DIRECTORY + f'/raw_gsam_data/2d/daily_2d/*.nc'
    files = sorted(glob(path))
    data = xr.concat(
        [xr.open_dataset(_)['LWNT'] for _ in files],
        dim='time'
    )
    data = data.coarsen({'lat': 25, 'lon': 25}).mean()
    return data

def load_gsam_reference_profiles():
    file = BASE_DIRECTORY + '/gsam_z_p_rho_reference.nc'
    return xr.open_dataset(file)

def load_gsam_eofs_pcs():
    file = BASE_DIRECTORY + '/gsam_coarse_eofs_pcs.nc'
    model = xe.single.EOF.load(file, engine='netcdf4')
    return model

def load_coarse_era5_w():
    path = BASE_DIRECTORY + '/raw_era5_data/coarsened_omega/*_w*.nc'
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
    path = BASE_DIRECTORY + f'/phase_composites/phase{phase}_composite_anomaly_{variable}.nc'
    return xr.open_dataarray(path)

def load_phase_composite_mean(variable, phase):
    path = BASE_DIRECTORY + f'/phase_composites/phase{phase}_composite_mean_{variable}.nc'
    return xr.open_dataarray(path)

def load_phase_composite(variable, phase):
    path = BASE_DIRECTORY + f'/phase_composites/phase{phase}_composite_{variable}.nc'
    return xr.open_dataarray(path)

def load_phase_transition_composite_anomaly(variable, phase, trans_type):
    path = BASE_DIRECTORY + f'/phase_composites/by_trans_type/phase{phase}_{trans_type}_composite_anomaly_{variable}.nc'
    return xr.open_dataarray(path)

def load_phase_transition_composite_mean(variable, phase, trans_type):
    path = BASE_DIRECTORY + f'/phase_composites/by_trans_type/phase{phase}_{trans_type}_composite_mean_{variable}.nc'
    return xr.open_dataarray(path)

def load_phase_transition_composite(variable, phase, trans_type):
    path = BASE_DIRECTORY + f'/phase_composites/by_trans_type/phase{phase}_{trans_type}_composite_{variable}.nc'
    return xr.open_dataarray(path)

def load_raw_ceres_data():
    path = BASE_DIRECTORY + f'/raw_ceres_data/northwest_tropical_pacific.CERES_SYN1deg-1H_Terra-Aqua-MODIS_Ed4.1_Subset_20200201-20200331.nc'
    return xr.open_dataset(path)

def load_coarse_gsam_2d():
    path = BASE_DIRECTORY + '/raw_gsam_data/coarsened_2d/*.nc'
    files = sorted(glob(path))
    data = xr.concat(
        [xr.open_dataset(_) for _ in files],
        dim='time'
    )
    return data

def load_imerg_data():
    path = BASE_DIRECTORY + '/raw_imerg_data/northwest_tropical_pacific.dyamond_time.imerg.nc'
    return xr.open_dataarray(path)

def load_era5_coarse_precip():
    path = BASE_DIRECTORY + '/raw_era5_data/coarsened_total_precip/coarsened_8.total_precip.202002.nc'
    return xr.open_dataarray(path)