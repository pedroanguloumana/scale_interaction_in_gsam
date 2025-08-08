# Functions for the generation of moisture space grids
#
import xarray as xr

def segment_data_into_grids(da, patch_length):

    lat_n = da.lat.size / patch_length
    lon_n = da.lon.size / patch_length

    coarsen_dict = {'lat': patch_length, 'lon': patch_length}
    tiled = (
        da
        .coarsen(coarsen_dict, boundary='exact')
        .construct({
            'lat': ('coarse_grid_lat', 'lat'),
            'lon': ('coarse_grid_lon', 'lon')
        })
        .stack({'coarse_grid': ['coarse_grid_lat', 'coarse_grid_lon']})
    )
    return tiled